# 12-support-ticket-router - Support Ticket Router with Human Support

- Седмица: 3 (Encorp AI Academy 2026)
- Домашно: задача 5
- Статус: `json-delivered`

## Условие (дословно)

Task:

1. Use a trigger that will pass support tickets (Chat, Webhook, Form, etc.)
2. Use Sentiment Analysis to assess urgency (add the appropriate sentiment categories)
3. Use Text Classifier to categorise by department (Sales, Technical, Billing, General)
4. Implement Human in the Loop that must confirm the sentiment category or change it. The change must be edited in the support ticket data
5. Use an AI Agent node with the proper instructions to process and answer the support ticket and use the following tools:
   1. Google Sheet tool - the agent will add the processed data to the sheet that will have the following columns: processing date, ticket text, sentiment category, department, AI Agent proposed answer.
   2. Google Tasks tool - add the ticket as a task in Google Tasks, with a short summary as the title and short task notes.

## Изисквания

| № | Изискване | Тип |
|---|-----------|-----|
| R1 | Тригер, който подава support тикети (Chat, Webhook, Form и др.) | задължително |
| R2 | Sentiment Analysis оценява спешността, с подходящи sentiment категории | задължително |
| R3 | Text Classifier разпределя по отдели: Sales, Technical, Billing, General | задължително |
| R4 | Human in the Loop: човек потвърждава или сменя sentiment категорията; промяната се записва в данните на тикета | задължително |
| R5 | AI Agent с подходящи инструкции обработва тикета и пише отговор | задължително |
| R6 | Google Sheets tool: агентът добавя ред с колони processing date, ticket text, sentiment category, department, AI Agent proposed answer | задължително |
| R7 | Google Tasks tool: тикетът се добавя като задача - кратко резюме за заглавие, кратки бележки | задължително |

## Уточнение на Здравко (2026-10-15)

Само Google Sheets може ли да е достатъчен? Изискване 4 иска след потвърждение/промяна категорията да се запази в тикета, но добра практика е оригиналът да се пази и да се знае кога какво е променено по тикета. (Допълнително изискване от Здравко, не от условието: одитна следа за промените.)

## Критерии за оценяване

_(не са посочени в условието)_
