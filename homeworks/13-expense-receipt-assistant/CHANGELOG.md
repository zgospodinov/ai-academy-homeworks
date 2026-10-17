# Changelog - 13-expense-receipt-assistant

## 2026-10-17 - 13-expense-receipt-assistant v2 (експорт на актуалните workflow-и)
- Промяна: `n8n-workflows/13-expense-receipt-assistant*.json` са заменени с експорт на живите workflow-и (основен `cOzlOG0ugCGic76O`, 35 нода; Spending Lookup `sz6oRpgEq17QjU1x`; Chat Agent `z6CUn8Ia5PZx4wgg`; Weekly Report `wVQNc1AMYVtN6G5y`; Error Alert `9A3TqOb0v0ZA1y78`). Новото спрямо v1: `Is Global Error` + `Raise Global Error` (глобални грешки на Read Receipt задействат Error workflow-а; потвърдено от Здравко), `Convert Amounts` в Spending Lookup и Weekly Report, `Manual Test Window`, node groups, актуални typeVersion от инстанса, бележка 10 за `pending` редове след грешка. Старите файлове са в `n8n-workflows/_versions/13-expense-receipt-assistant*/v1.json`.
- Санитизиране: Telegram chat id -> `YOUR_TELEGRAM_CHAT_ID`, `managerEmail`/`financeEmail` -> плейсхолдъри, `formUrl` -> `https://YOUR-N8N-DOMAIN/form/expense-receipt`, имена на credentials обезличени, `errorWorkflow` махнат от settings. След импорт: избери credentials, попълни тези стойности и избери Expense Error Alert като Error workflow.
- Причина: JSON файловете в репото бяха остарели след корекциите, направени директно в n8n.
- Засегнати нодове: Is Global Error, Raise Global Error, Convert Amounts, Manual Trigger, Manual Test Window (нови); Config Report, Last Week Final Only, Read Receipt (променени).

## 2026-10-17 - 13-expense-receipt-assistant v1 (tested)
- Промяна: потвърдено от Здравко, че основният поток работи правилно за всички сценарии от `test-data/test-scenarios.md`, а чат агентът и седмичният отчет работят след поправките. Статус -> tested. Поправки в n8n след първите тестове: (1) Expense Spending Lookup и Expense Weekly Report - нов нод `Convert Amounts` (Set) преди `Summarize`, защото колоните на `expenses` са текст, а Summarize сумира само числа (чатът връщаше 0.00); (2) Expense Weekly Report - `Last Week Final Only` с Always Output Data и нов нод `Manual Test Window` (ръчно пускане = последните 7 дни, етикет TEST; Monday Schedule остава с предишната календарна седмица); (3) нова тестова бележка `receipt_07_hotel_pirin.jpg` (сценарий 7).
- Причина: резултати от тестовете на Здравко в неговия n8n.
- Засегнати нодове: Convert Amounts (нов, 2 workflow-а), Manual Test Window (нов), Config Report, Last Week Final Only.
- Отворено: Error Alert е потвърден във v2; JSON файловете са заменени с експорт във v2.

## 2026-10-17 - 13-expense-receipt-assistant v1 (MCP доставка)
- Промяна: петте workflow-а са създадени директно в n8n през MCP (непубликувани, личен проект, таг `encorp-homework`, node groups + Sticky Notes). Ids: основен `cOzlOG0ugCGic76O` (33 нода), Spending Lookup `sz6oRpgEq17QjU1x`, Chat Agent `z6CUn8Ia5PZx4wgg`, Weekly Report `wVQNc1AMYVtN6G5y`, Error Alert `9A3TqOb0v0ZA1y78`. Използвани са съществуващите Data Tables `expenses` и `expense_policy` (всички колони на `expenses` са текст -> `String()`/`Number()`). Версиите на нодовете са от инстанса (formTrigger 2.6, switch 3.4, chatTrigger 1.5, memoryBufferWindow 1.4, executeWorkflowTrigger 1.2). Не е тестван.
- Причина: искане на Здравко - създаване през n8n MCP конектора.
- Засегнати нодове: всички нови. Групата "Read and validate receipt" не е реализирана като node group (смесени клонове нарушават правилото за един вход/изход) - остава Sticky Note.
- Отворено: JSON файловете в `n8n-workflows/` още са генерираните от скрипта (по-стари typeVersion) - да се презапишат от `get_workflow_details` след първия успешен тест.

## 2026-10-16 - 13-expense-receipt-assistant v1
- Промяна: нов домашен (седмица 3, задача 6) - основен workflow (Form Trigger, vision Basic LLM Chain + Structured Output Parser, Data Tables `expenses` и `expense_policy`, Switch, Gmail Send and Wait с Custom Form) и 4 бонус workflow-а (седмичен отчет, чат агент със sub-workflow tool, Error Alert). Не е тестван.
- Причина: ново домашно; план одобрен от Здравко 2026-10-16.
- Засегнати нодове: всички нови.

