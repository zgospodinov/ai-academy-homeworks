"""Конвертира PDF в чист текст с маркери [Страница N] (нужен: pdftotext от poppler-utils).

Употреба:
  python pdf_to_text.py FILE.pdf [OUT.txt] [--pages N]

--pages N записва само първите N страници (за бърз смоук тест на Ingest).
PDF и получените .txt не се качват в репото (виж .gitignore в корена).
"""
import re, subprocess, sys

args = [a for a in sys.argv[1:] if not a.startswith("--")]
src = args[0]
dst = args[1] if len(args) > 1 else src.rsplit(".", 1)[0] + ".txt"
limit = None
if "--pages" in sys.argv:
    limit = int(sys.argv[sys.argv.index("--pages") + 1])
    if str(limit) in args:
        args.remove(str(limit))
        dst = args[1] if len(args) > 1 else src.rsplit(".", 1)[0] + f"_first{limit}pages.txt"

raw = subprocess.run(["pdftotext", src, "-"], capture_output=True, text=True, check=True).stdout
pages = raw.split("\f")
if pages and not pages[-1].strip():
    pages = pages[:-1]
out = []
for i, page in enumerate(pages, 1):
    if limit and i > limit:
        break
    page = re.sub(r"[ \t]+\n", "\n", page)
    page = re.sub(r"\n{3,}", "\n\n", page).strip()
    if page:
        out.append(f"[Страница {i}]\n{page}")
open(dst, "w", encoding="utf-8").write("\n\n".join(out) + "\n")
print(f"{len(out)} страници с текст -> {dst}")
