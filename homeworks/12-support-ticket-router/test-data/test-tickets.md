# Тестови тикети - 12-support-ticket-router (v2)

Очакваните категории са ориентировъчни (LLM е вероятностен). Пускай workflow-а през Test URL на `Ticket Form`; когато стигне до `Request Sentiment Review`, отвори линка от имейла (бутон "Open review form") и изпрати формата.

| № | Тикет | Очаквано (AI) |
|---|-------|---------------|
| 1 | Whole production is down, our customers cannot log in and we lose money every minute. Fix this NOW or we cancel the contract. | Urgent, Technical |
| 2 | I was charged twice for my March subscription. This is the second time it happens. Please fix it. | Frustrated, Billing |
| 3 | Hi, what are your enterprise pricing tiers and is there a demo available? | Neutral, Sales |
| 4 | Thanks a lot, the new report feature is great! | Positive, General |
| 5 (граничен) | help | Neutral, General (без срив) |
| 6 (български) | Здравейте, не мога да вляза в профила си от вчера и имам фактура за плащане до утре. | Urgent или Frustrated, Technical |

## Сценарии за ревюто
1. **Потвърждение:** тикет 3, избираш `Neutral`. Очаквано: `Audit Log` -> `Changed = No`; `Tickets` -> `Neutral`.
2. **Смяна:** тикет 2 (AI: Frustrated), избираш `Urgent` и бележка. Очаквано: `Tickets` -> `Urgent`; `Audit Log` -> `Sentiment AI = Frustrated`, `Sentiment Final = Urgent`, `Changed = Yes`, бележката; в Executions данните на `Apply Review` имат `sentimentOriginal`, `sentiment`, `sentimentChanged = true`.
3. **Форма от имейла, втори път:** отвори линка отново след изпращане. Очаквано: n8n не приема втори отговор (поведение на Send and Wait; не е потвърдено).
4. **Два чакащи тикета:** пусни тикети 1 и 3, ревюирай ги в обратен ред. Очаквано: двата стигат до края независимо един от друг; в Executions са два "Waiting".
5. **Без ревю:** не отваряй формата. Очаквано: изпълнението остава "Waiting", нищо не се записва в Sheets.
6. **Ключ на Custom Form:** в Executions виж изхода на `Request Sentiment Review`; ако стойността не е в `data['Sentiment category']`, оправи израза в `Read Review Decision` (резервът по стойност трябва да я намери).
7. **Google Tasks:** задачата е със заглавие `[Department] ...` до 80 знака и кратки бележки.
8. **HTML в тикета:** тикет с `<b>x</b> =1+1` - в имейла е като текст, в Sheets е като текст (не формула).
