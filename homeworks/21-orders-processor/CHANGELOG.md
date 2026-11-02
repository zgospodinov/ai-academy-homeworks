# Changelog - 21-orders-processor

## 2026-11-02 - 21-orders-processor v5.1 (документация и setup)
- Промяна: два нови Sticky Note-а в основния workflow - "Стратегия за обработка на грешки" и "Prerequisites" (какво остава ръчно при нова инстанция).
- Промяна: `homeworks/21-orders-processor/setup/` - CSV шаблони за Data Tables (`orders_eval_dataset`, `orders_eval_images`, `orders_ledger`) и за табовете на Google Sheet, SQL за Supabase, README.
- Причина: бърз сетъп на нова n8n инстанция без ръчно създаване на таблици.
- Засегнати нодове: Sticky Error Strategy, Sticky Prerequisites (само бележки).
- Промяна (подредба): възлите на основния workflow са преподредени - групите са подредени една под друга, във всяка нодовете вървят отляво надясно по дълбочина на потока, AI под-нодовете са под агента, нищо не се припокрива; нов Sticky Note "4b. Защита от дубликати"; Guard Auth бележката е при другите бележки горе.

## 2026-11-02 - 21-orders-processor v5 (error handling и идемпотентност)
- Промяна: ledger в Data Table `orders_ledger`. След одобрение ключ SHA256 (сесия, получател, тема, текст, срок) -> статус new/claimed/sent/logged. Преди Gmail редът се заявява (`claimed`); при `claimed` се проверява Gmail Sent и имейлът не се праща втори път; `sent` води само до запис в Sheets; `logged` връща "вече е изпратена".
- Промяна: Sheets запис е `appendOrUpdate` по `po_number` + `line_no` (повторен опит не дублира редове); номерът на поръчката е стабилен (`PO-дата-хеш`).
- Промяна: Gmail без автоматичен retry; при грешка `continueErrorOutput` -> съобщение в чата + Stop and Error -> Error Handler. Втори опит е безопасен заради ledger-а.
- Промяна: retry 3 опита с пауза (1-3 s) за Agent, Guard MCP клиентите, четенето от Sheets, Postgres и Data Table, upsert-а в Sheets и ledger update-ите; `maxRetries` на модела 0, за да не се трупат слоеве.
- Промяна: Error Workflow е зададен на всички потоци освен самия Error Handler; Error Handler, Guard MCP Server и Guard Check са публикувани (Error Workflow изисква публикуван handler; Guard е нужен за eval).
- Резултат: Eval Runner 16/16 (изпълнение 10677). Ledger пътят не е тестван от край до край в чата (нужно е одобрение), виж `test-plan.md`.
- Бележка: Suppliers Sync е на 5 минути; при постоянна грешка ще праща алерт на всеки цикъл (няма ограничаване на честотата).

## 2026-11-02 - 21-orders-processor v4 (имена на нодовете)
- Промяна: всички нодове в 6-те workflow-а са във формат `Оригинално име - кратко описание` (напр. `Edit Fields - Count Attempt`, `If - Can Retry`, `AI Agent - Order Assistant`); sticky notes са непроменени. Изключение: `check_text` в Guard MCP Server, защото името на нода е името на MCP инструмента.
- Промяна: препратките в изразите (`$("...")`) и в Code нодовете са пренаписани към новите имена; `solution-plan.md`, `test-plan.md` и Mermaid схемата са обновени.
- Причина: нодът да се разбира от името му, без да се отваря.
- Проверка: Eval Runner 16/16 (изпълнения 10364 и 10441); няма висящи препратки, свързванията са същите (68), позициите са непроменени.
- Бележка: преименуването в n8n (`renameNode`) НЕ обновява препратките в изразите - те се пренаписват отделно.
- Проверка на Suppliers Sync след преименуването: ръчно пълно прекодиране (изп. 10522) - хешът е записан в `supplier_sync_state`, `supplier_chunks` има 10 реда.
- Всичките 6 workflow-а са непубликувани (по искане на Здравко, 2026-11-02).

## 2026-11-01 - 21-orders-processor v3 (стабилност на evaluations)
- Промяна: `Agent Chat Model` отново е `openai/gpt-4.1-mini` (в workflow-а се беше върнал gpt-4o-mini), температура 0; `Supplier Search` topK 5; в системния промпт правило 2 е уточнено (един запис е един доставчик, пример за малко име с двама доставчици), правило 3 без фиксиран брой резултати.
- Промяна: Guard Check има custom prompt на Guardrails нода (само явни опити за разкриване на инструкции, смяна на роля, пренасочване на получателя); публикуван.
- Промяна: в eval режим празен изход на агента се записва като резултат от случая (`Empty Output Result`), а не прекъсва изпълнението; 7 лентови стикита в основния workflow.
- Причина: прогоните колебаеха (9-14 от 16): фалшиво двусмислие за Мария Колева, празен изход (Output Parser отхвърля отговора) и фалшиво блокиране на E03.
- Резултат: 16/16 в два последователни прогона; предишно състояние 11-15/16 (виж `test-plan.md`).
- Засегнати нодове: Agent Chat Model, Supplier Search, Order Agent (prompt), Empty Output Result, Check Jailbreak (Guard Check).
- Бележка: пълният чат поток с одобрение остава за ръчен ретест; `adminChatId` в Error Handler е placeholder.

## 2026-10-30 - 21-orders-processor v2 (evaluations, дати, организация)
- Промяна: нативни n8n Evaluations върху Data Table `orders_eval_dataset` (16 случая) и Eval Runner, който пуска всички случаи и записва `eval_results` (16/16 успешни); снимките за тестовете са в Data Table `orders_eval_images`.
- Промяна: детерминирани дати (`delivery_when` + Luxon, Europe/Sofia); снимките се прикачват към всяко извикване на агента; по един ред на артикул в `purchase_orders`.
- Промяна: модел `openai/gpt-4.1-mini`; Guard threshold 0.9; правила в system prompt за двусмислен и непознат доставчик, непразен `message`, съобщение без поръчка.
- Промяна: Suppliers Sync засича промени с хеш на таба `suppliers` на всеки 5 минути (вместо Sheets Trigger); Error Handler и Guard Check с контекст за повторните опити.
- Промяна: всички 6 workflow-а в n8n папка `Week 05 - HW 01 - Orders Processor`; JSON копия в `n8n-workflows/21-orders-processor*.json`; `solution-plan.md` и `assignment.md` обновени.
- Причина: домашното изисква проверим резултат и стабилни дати; автоматичните тестове показаха проблеми, поправени в промпта и прага.
- Засегнати нодове: Config, Build Eval Input, Compute Delivery Date, Validate Draft, Eval Scores, Eval Verdict, Order Agent (prompt), Agent Chat Model, Guard Check (threshold), Count Attempt, Can Retry?.
- Бележка: пълният чат поток с одобрение след промените на датите и снимките не е ретестван ръчно. T9, T11, T12, T13 са ръчни (виж `test-plan.md`). В Error Handler `adminChatId` е placeholder в JSON.

## 2026-10-29 - 21-orders-processor v1
- Промяна: първо изграждане през n8n MCP по одобрения план (Chat Trigger, Order Agent с Supabase RAG, Guard през MCP, Error Handler, Suppliers Sync).
- Причина: домашно седмица 5, задача 1.
- Засегнати нодове: всички.
