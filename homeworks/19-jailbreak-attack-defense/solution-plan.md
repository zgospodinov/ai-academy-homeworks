# 19-jailbreak-attack-defense - Solution plan

- Статус: `json-delivered` (план одобрен от Здравко на 2026-10-23, след промяна: нод 2 е Data Table; workflow създаден през MCP, id `A2fA5mRuaSrTnjLF`, непубликуван; изпълнения #2881 и #2885, виж `results.md`)
- Версия: v1
- Workflow: `Encorp | Homework | Week 04 | HW 06 | Jailbreak Attack Defense`, таг `encorp-homework`
- Промптове: `system-prompt-basic.md`, `system-prompt-hardened.md`; тестове: `test-plan.md`; тестови данни: `test-data/test-cases.csv`

## Изисквания

R1 базов AI агент със семпъл system prompt; R2 jailbreak с поне две техники (Role-Playing Bypass, Reverse Psychology); R3 документирани промптове и отговори; R4 system prompt с Prompt Hardening; R5 същите промптове втори път и документиран резултат. Подробно: `assignment.md`.

## Идея

Тестова обвивка: една таблица с атаки се пуска срещу два агента с еднакъв модел - базов и с guardrails. Агентът е support бот "Nova" на фиктивната фирма NovaTech, с фиктивен таен код в промпта. Пробив = изтича кодът или агентът излиза от ролята (проверява се автоматично с "канарчета" и после се чете на ръка).

## Схема

```mermaid
flowchart LR
    T1(["1. Manual Trigger"]) --> N2[("2. Get Test Cases")]
    subgraph G1["Attack - Basic Agent"]
        N3{{"3. Basic Agent"}} --> N5["5. Keep Basic Reply"]
        N4{{"4. Basic Chat Model"}} -.->|ai_languageModel| N3
    end
    subgraph G2["Defense - Hardened Agent"]
        N6{{"6. Hardened Agent"}} --> N8["8. Keep Hardened Reply"]
        N7{{"7. Hardened Chat Model"}} -.->|ai_languageModel| N6
    end
    subgraph G3["Scoring"]
        N9["9. Score Replies"] --> N10["10. Summarize Breaches"]
    end
    N2 --> N3
    N5 --> N6
    N8 --> N9
    classDef trigger fill:#e8f0fe,stroke:#4a6fa5
    classDef ai fill:#f3e8ff,stroke:#7c4dbb
    class T1 trigger
    class N3,N4,N6,N7 ai
```

## Нодове

| № | Група | Нод | Защо е тук | Ключови параметри | Покрива |
|---|-------|-----|-----------|-------------------|---------|
| 1 | - | Manual Trigger | Тестът се пуска ръчно | - | R3, R5 |
| 2 | - | Get Test Cases (Data Table) | Атаките са редове в таблицата `jailbreak_test_cases`: лесно за корекция, допълване и преглед | Get row(s), Return All | R2, R3 |
| 3 | Attack | Basic Agent (`agent`) | Базов агент със семпъл промпт | `text = {{ $json.prompt }}`, system message от `system-prompt-basic.md` | R1, R2 |
| 4 | Attack | Basic Chat Model | Моделът на агента | gpt-4o-mini, temp 0.7 | R1 |
| 5 | Attack | Keep Basic Reply (Set) | Агентът връща само `output`; пази контекста на случая | `basicReply` | R3 |
| 6 | Defense | Hardened Agent | Същият агент с guardrails | system message от `system-prompt-hardened.md` | R4, R5 |
| 7 | Defense | Hardened Chat Model | Същият модел и настройки | gpt-4o-mini, temp 0.7 | R4 |
| 8 | Defense | Keep Hardened Reply (Set) | Пази втория отговор до първия | `hardenedReply` | R5 |
| 9 | Scoring | Score Replies (Code) | Пробив/без пробив за всеки агент (код, маркер; за контрола - очакван низ) | числови полета 0/1 | R3, R5 |
| 10 | Scoring | Summarize Breaches | Брой пробиви по атака и агент | Sum, групиране по `caseId` | R5 |

## Таблица `jailbreak_test_cases`

Колони: `caseId` string, `run` number, `technique` string, `kind` string (`attack`/`control`), `prompt` string, `marker` string. Първоначално 15 реда (5 случая x 3 пускания); след изпълнение #2881 са добавени A5, A6, A7 (още 9 реда, общо 24), защото базовият агент устоя на A1-A4 (ескалацията е предвидена в плана). След изпълнение #2885 са добавени и A5b, A5c, A5d по 5 пускания (още 15 реда, общо 39) по искане на Здравко. Виж `test-data/test-cases.csv`.

## Допускания (от assignment.md)

Q2 support бот със секрет и Q3 тестова обвивка с 2 агента - отговори на Здравко. Q4-Q8 приети с одобрението на плана: техники A1 Role-Playing Bypass и A2 Reverse Psychology, бонус A3 Instruction Override и A4 Role-Play извън темата; gpt-4o-mini temp 0.7 за двата агента; по 3 пускания; безобиден експеримент с фиктивен код; атаки на английски, документация на български.

## Credentials

`OpenRouter Encorp Academy Homeworks` (свързан).

## Покритие

R1 -> нодове 3-4. R2 -> нодове 2-3. R3 -> нодове 2, 5, 8, 9 и `results.md`. R4 -> нодове 6-7 и `system-prompt-hardened.md`. R5 -> нодове 6, 8-10.

## Режим на доставка

Директно в n8n през MCP (личен проект, непубликуван) + санитизиран JSON в `n8n-workflows/19-jailbreak-attack-defense.json`. Data Table `jailbreak_test_cases` се създава през MCP. Тестът се пуска през `execute_workflow` в `manual` режим (разход: около 30 извиквания на gpt-4o-mini).

## Ограничение

Тайният код стои в промпта и при двата агента. Hardening намалява риска, но не го елиминира; пълната защита е секретът да не е в промпта.
