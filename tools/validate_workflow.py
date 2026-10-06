"""Validate and sanitize n8n workflow exports.
  python tools/validate_workflow.py FILE...            # check only
  python tools/validate_workflow.py --sanitize FILE... # check, clean in place, check again
  Add --strict to also clear credential ids and meta.instanceId (generic exports; not a security need).
"""
import json, re, sys

EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
SECRET = re.compile(r"sk-[A-Za-z0-9_-]{16,}|AIza[0-9A-Za-z_-]{20,}|Bearer\s+[A-Za-z0-9._-]{20,}|ghp_[A-Za-z0-9]{20,}|xox[bap]-[A-Za-z0-9-]{10,}|\d{8,10}:[A-Za-z0-9_-]{30,}")
PLACEHOLDER_EMAIL = "you@example.com"

def check(d):
    err, warn = [], []
    nodes = d.get("nodes", [])
    names = [n.get("name") for n in nodes]
    if len(set(names)) != len(names): err.append("duplicate node names")
    ids = [n.get("id") for n in nodes]
    if len(set(ids)) != len(ids): err.append("duplicate node ids")
    for n in nodes:
        for k in ("id", "name", "type", "typeVersion", "position", "parameters"):
            if k not in n: err.append(f"{n.get('name')}: missing {k}")
    linked = set()
    for src, kinds in d.get("connections", {}).items():
        if src not in names: err.append(f"connection from unknown node {src}")
        linked.add(src)
        for kind, branches in kinds.items():  # main, ai_languageModel, ai_tool, ai_outputParser...
            for branch in branches or []:
                for c in branch or []:
                    if c["node"] not in names: err.append(f"{src} -> unknown node {c['node']}")
                    linked.add(c["node"])
    for n in nodes:
        if n["name"] not in linked and "stickyNote" not in n["type"] and len(nodes) > 1:
            err.append(f"orphan node {n['name']}")
        if n.get("disabled"): warn.append(f"disabled node {n['name']}")
        for k, v in (n.get("parameters") or {}).items():
            if isinstance(v, str) and "{{" in v and not v.startswith("="):
                warn.append(f"{n['name']}.{k}: expression without leading '='")
        for t, c in (n.get("credentials") or {}).items():
            if re.search(r"account\s+\S", c.get("name", ""), re.I): warn.append(f"{n['name']}: credential name '{c['name']}' may contain a personal name")
    if not any(re.search(r"trigger|webhook", n["type"], re.I) for n in nodes): err.append("no trigger node")
    if d.get("pinData"): warn.append("pinData is not empty")
    raw = json.dumps(d, ensure_ascii=False)
    if SECRET.search(raw): err.append("possible secret in JSON - STOP and tell the user")
    if EMAIL.search(raw.replace(PLACEHOLDER_EMAIL, "")): warn.append("email address present")
    return err, warn

def sanitize(d, strict=False):
    """Clean the export. Never touches secrets: those must be reviewed by a human."""
    done = []
    if d.get("pinData"): d["pinData"] = {}; done.append("pinData emptied")
    if strict and "instanceId" in d.get("meta", {}): del d["meta"]["instanceId"]; done.append("meta.instanceId removed")
    for n in d.get("nodes", []):
        for t, c in (n.get("credentials") or {}).items():
            if strict and c.get("id"): c["id"] = ""; done.append(f"{n['name']}: credential id cleared")
            new = re.sub(r"(account)\s+\S.*$", r"\1", c.get("name", ""), flags=re.I)
            if new != c.get("name"): c["name"] = new; done.append(f"{n['name']}: credential name -> '{new}'")
    def walk(x):
        if isinstance(x, dict): return {k: walk(v) for k, v in x.items()}
        if isinstance(x, list): return [walk(v) for v in x]
        if isinstance(x, str) and EMAIL.search(x) and "{{" not in x:
            done.append("email replaced with placeholder"); return EMAIL.sub(PLACEHOLDER_EMAIL, x)
        return x
    d = walk(d)
    return d, sorted(set(done))

if __name__ == "__main__":
    args = sys.argv[1:]
    do_clean = "--sanitize" in args
    strict = "--strict" in args
    files = [a for a in args if not a.startswith("--")]
    rc = 0
    for p in files:
        d = json.load(open(p, encoding="utf-8"))
        if do_clean:
            d, done = sanitize(d, strict)
            json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
            open(p, "a").write("\n")
            for x in done: print(f"   cleaned: {x}")
        err, warn = check(d)
        print(("ERROR " if err else "OK    ") + p)
        for e in err: print("   ERR ", e)
        for w in warn: print("   warn", w)
        rc |= bool(err)
    sys.exit(rc)
