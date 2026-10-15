# Очаквани резултати - 11-meeting-notes-summariser

Пускане: Execute workflow върху `Morning Schedule` (дава `timestamp`). Резултатите са очаквания за формата, не записани изходи; текстът на резюметата варира между изпълненията.

## Основен поток
| Нод | Очакване |
|-----|----------|
| Collect Meeting Notes | 4 items: Engineering, Sales, HR, Finance (~1200-1400 знака всяка) |
| Summarize Each Meeting | 4 items с `response` (или `output`), до 5 точки, с отговорници и срокове |
| Aggregate Meeting Summaries | 1 item, `meetings` = масив от 4 `{department, summary}` |
| Summarize All Meetings | 1 item: кратък абзац + `Cross-team dependencies:` + `Top risks:` |
| Format Date | `formattedDate`, напр. `Wednesday, 14 October 2026` |
| Attach Date To Summary | `reportDate`, `title`, `generalSummary`, `departmentSummaries` (4 обекта) |

## Междуотдеални зависимости, заложени в бележките
- Sales обещава Northwind (340k EUR) bulk-export API до края на октомври, а Engineering го мести в 4.3 (не преди средата на ноември).
- Senior backend позиция: Engineering -> HR -> Finance (решение не преди следващия понеделник).
- 10% отстъпка за SMB: Sales -> Finance (анализ на маржа до сряда).
- Q4 прогнозата на Finance предполага, че Northwind се затваря през октомври.
Добро общо резюме трябва да улови поне 2 от тях.

## Гранични случаи
1. Кратка бележка (1 chunk): Map Reduce пак връща резюме (скъсете една бележка в Code нода).
2. `runComparison` = false в Config: клонът `Run Comparison?` -> ... не се изпълнява.

## Бонус (Build Comparison)
3 items в ред Stuff, Refine, Map Reduce с полета `method`, `estimatedChunks`, `estimatedLlmCalls`, `summaryChars`, `summary`. Очаквани брой извиквания: Stuff = 1, Refine = chunks, Map Reduce = chunks + 1. Времето на всеки нод се чете в n8n и се записва в `comparison.md` (създава се след изпълнение).
