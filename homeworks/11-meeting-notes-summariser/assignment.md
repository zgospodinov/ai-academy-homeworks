# 11-meeting-notes-summariser - Meeting Notes Summariser

- Седмица: 3 (Encorp AI Academy 2026)
- Домашно: задача 4
- Статус: `tested`

## Условие (дословно)

Task:

1. Use an AI model - ChatGPT, Gemini, Claude, etc. to generate 3-4 meeting notes from different company departments.
2. Use a Schedule Trigger to simulate collecting morning meeting notes in a company.
3. Pass the meeting notes from a Code or Edit node to be processed by the workflow
4. Use a Summarisation Chain with "Map Reduce" option to summarise the meetings separately and make a general summary of all morning meetings
5. Use a Date and Time Node to get the timestamp from the Schedule trigger and format the date to a format of choice
6. Use an Edit node to attach the date to the summary.

Bonus:

1. Compare different summarisation methods (Map Reduce vs Refine vs Stuff)

## Изисквания

| № | Изискване | Тип |
|---|-----------|-----|
| R1 | 3-4 бележки от срещи от различни отдели, генерирани с AI модел | задължително |
| R2 | Schedule Trigger, който симулира събирането на сутрешните бележки | задължително |
| R3 | Бележките се подават към потока от Code или Edit нод | задължително |
| R4 | Summarization Chain с Map Reduce: резюме на всяка среща поотделно + общо резюме на всички сутрешни срещи | задължително |
| R5 | Date & Time нод взима timestamp от Schedule Trigger и го форматира във формат по избор | задължително |
| R6 | Edit нод прикачва датата към резюмето | задължително |
| R7 | Сравнение на Map Reduce / Refine / Stuff | бонус |

## Критерии за оценяване

_(не са посочени в условието)_
