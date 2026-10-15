# Solution plan - 11-meeting-notes-summariser

- Статус: `tested` (плана е одобрен от Здравко 2026-10-14; главният поток работи по думите му, бонус клонът е изпълнен)
- Версия: v2 (v1 е в `n8n-workflows/_versions/11-meeting-notes-summariser/v1.json`)
- Workflow: `Encorp | Homework | Week 03 | HW 04 | Meeting Notes Summariser` (`n8n-workflows/11-meeting-notes-summariser.json`)
- Таг: `encorp-homework`

## Изисквания
R1-R7 са в `assignment.md`.

## Схема
```
Morning Schedule -> Config -> Collect Meeting Notes (Code, 4 items)
   |- Summarize Each Meeting (Map Reduce, 1 run на среща) -> Label Department Summaries
   |     -> Aggregate Meeting Summaries -> Prepare Overall Input
   |     -> Summarize All Meetings (Map Reduce) -> Format Date -> Attach Date To Summary
   `- (бонус) Run Comparison? (IF) -true-> Aggregate Notes For Comparison -> Prepare Comparison Input
         -> Summarize Stuff / Summarize Refine / Summarize Map Reduce (паралелно)
         -> Merge Results (Append, 3) -> Build Comparison

OpenRouter Chat Model (ai_languageModel) -> петте Summarization Chain нода
```

## Нодове
| № | Нод | Защо | Ключови параметри | Покрива |
|---|-----|------|-------------------|---------|
| 1 | Morning Schedule (Schedule Trigger 1.4) | Симулира сутрешното събиране, дава `timestamp` | всеки ден 10:00; timezone на workflow-а `Europe/Sofia`; пуска се ръчно с Execute workflow (няма Manual Trigger, защото не дава timestamp) | R2 |
| 2 | Config (Set) | Превключвател за бонуса | `runComparison` = true | R7 |
| 3 | Collect Meeting Notes (Code) | 4 items `{department, notes}`; Code, защото Set прави един item | бележки, генерирани с Claude; guard за празен текст | R1, R3 |
| 4 | Summarize Each Meeting (Summarization Chain v2) | Резюме на всяка среща отделно; всяка бележка е над 1000 знака -> поне 2 chunk-а | Node Input (JSON), Simple 1000/200, `map_reduce`, свои prompt-ове | R4 |
| 5 | OpenRouter Chat Model | Един модел за всички chain-ове | temperature 0, Max Retries 3 | R4 |
| 6 | Label Department Summaries (Set) | Chain връща само `response`/`output`; отделът се връща по индекс | `$('Collect Meeting Notes').all()[$itemIndex]` | R4 |
| 7 | Aggregate Meeting Summaries | 4 резюмета -> масив `meetings` | All Item Data | R4 |
| 8 | Prepare Overall Input (Set) | Един текст `### Dept\nрезюме` (без двойно стрингифициране на масива) | само `meetingsText` | R4 |
| 9 | Summarize All Meetings (Summarization Chain v2) | Общо резюме | Simple 800/100, `map_reduce` | R4 |
| 10 | Format Date (Date & Time 2) | Форматира timestamp-а на тригера | Format a Date, Custom `EEEE, dd MMMM yyyy`, `formattedDate`, Include Input Fields | R5 |
| 11 | Attach Date To Summary (Set) | Финален обект | `reportDate`, `title`, `generalSummary`, `departmentSummaries` | R6 |
| 12-18 | Бонус: Run Comparison? (IF), Aggregate Notes For Comparison, Prepare Comparison Input, Summarize Stuff / Refine / Map Reduce, Merge Results, Build Comparison | Един вход, три метода; Build Comparison дава `method`, `estimatedChunks`, `estimatedLlmCalls`, `summaryChars`, `summary` | Simple 500/100, идентични инструкции във всички методи | R7 |
| 19 | Sticky Note | Схема и покритие | | всички |

## Допускания и credentials
- Credentials: OpenRouter (`OpenRouter Encorp Academy Homeworks`, id от предишните експорти на Здравко).
- Summarization Chain typeVersion 2 (потвърдена от документацията и кода на n8n, но не и от импорт). Версия 2.1 с batching връща `output` вместо `response`; затова се чете `$json.response ?? $json.output`.
- Параметрите на Date & Time (`operation: formatDate`, `customFormat`, `options.useWorkflowTimezone`) НЕ са потвърдени от източник; при празни полета след импорт - експорт на нода.
- Self-hosted: няма webhook и OAuth.
- Общото резюме е върху 4-те резюмета (не върху суровите бележки): по-евтино и всеки отдел тежи еднакво.
- Един Chat Model е свързан към 5 chain-а; ако UI го отхвърли, се дублира.

## Тестов план
Виж `test-data/expected-results.md`; входът е `test-data/meeting-notes.md`.

## Покритие
R1 -> 3, R2 -> 1, R3 -> 3, R4 -> 4-9, R5 -> 10, R6 -> 11, R7 -> 12-18.

## v2 (2026-10-14)
Изходът на Summarization Chain v2 е обект (`{text}` / `{output_text}`), затова нодовете 6, 11 и Build Comparison го четат с `$json.response?.text ?? $json.response?.output_text ?? ...`. Резултатът от бонуса е в `comparison.md`. Главният поток (нодове 1-11) е работил и във v1 (Здравко, 2026-10-15), т.е. Set нодовете не са гърмели; поправката им е за чист текст в полетата и не е препроверена с отделно изпълнение на v2. Бонус клонът е изпълнен.
