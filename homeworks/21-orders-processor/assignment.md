# 21-orders-processor - Orders Processor

- Седмица: 5
- Домашно: задача 1
- Статус: `plan-approved`

## Условие (дословно)

Седмица 5, Задача 1: "Orders Processor"

A client (commercial sphere of your choice - books, car parts, computers, smartphones, etc.) has asked you to assist them in creating an AI automation for processing the orders they make to suppliers in order to maintain their business running smoothly.
They need an AI automation system that will accept a user input with basic order data on which an AI Agent with access to the RAG database will draft an email and return the draft to the user for approval. If the user approves it - it has to be sent automatically to the designated email address and logged as a purchase order in a Google Sheet database. There must be an error workflow that will handle and notify the user for the errors that might occur and jailbreak prevention mechanism to stop jailbreak attacks.

Пълните технически изисквания: `attachments/Orders_Processor_Technical_Specs.md`.

## Изисквания

| № | Изискване | Тип |
|---|-----------|-----|
| R1 | Интерфейс за вход: Form / Chat / Telegram / Discord / Slack или комбинация | задължително |
| R2 | AI Agent обработва входа и връща чернова на имейл, ако има цялата нужна информация | задължително |
| R3 | Agent обработва прикачена снимка на артикула и я добавя към контекста на заявката | задължително |
| R4 | Agent задава въпроси, ако липсва доставчик в RAG или информация (липсваща информация може да се пропусне, ако потребителят поиска) | задължително |
| R5 | Имейлът се изпраща САМО при изрично потвърждение от потребителя; чернова може да се коригира | задължително |
| R6 | Черновата показва: имейл на получателя, тема, тяло, снимка на артикула (ако има) | задължително |
| R7 | RAG векторна база с доставчици: фирма, лице за контакт, имейл | задължително |
| R8 | Търсене в RAG: едно лице -> фирма и имейл; няколко лица с едно име -> въпрос към потребителя; няма такъв -> съобщение и искане на имейл директно | задължително |
| R9 | Задължителни полета: лице/фирма, артикул, количество, дата на доставка, дали е нужно писмено потвърждение | задължително |
| R10 | Дата на доставка винаги като ден от седмицата + дата ("утре", "следващия понеделник", "след 5 дена" -> с дата) | задължително |
| R11 | Error workflow: логва грешките и праща съобщение с детайли | задължително |
| R12 | Празен изход (empty object) от Agent = грешка; съобщението на потребителя се подава отново за обработка | задължително |
| R13 | Jailbreak защита (вход и/или изход), поне един механизъм; опитите се спират | задължително |
| R14 | Jailbreak опитите се логват в проста Google Sheet таблица | задължително |
| R15 | След потвърждение: имейлът (с прикачена снимка, ако има) се изпраща на доставчика | задължително |
| R16 | Поръчката се логва в Google Sheet с цялата информация за проследяване | задължително |

Критерии за оценяване: не са дадени.

## Отворени въпроси

| № | Въпрос / неяснота | Засяга | Тежест | Предложено допускане | Статус | Отговор |
|---|-------------------|--------|--------|----------------------|--------|---------|
| Q1 | Седмица и номер на задачата | име | блокиращ | Седмица 5, задача 1 | answered | От съобщението на Здравко |
| Q2 | Интерфейс: Telegram бот или Chat Trigger | R1, R3, R12 | блокиращ | Telegram | answered | Chat Trigger (публичен, Response Mode = responseNodes, Allow File Uploads) и Chat нодове за всички съобщения към потребителя (Send a message, Send message and wait for response). Здравко потвърди със скрийншот, че нодовете са налични (2026-10-29) |
| Q3 | Google Sheet: един документ с табове `purchase_orders`, `jailbreak_log`, `error_log` | R14, R16 | блокиращ за доставката | Създава се през Drive | answered | Създаден през Drive (2026-10-29) в Drive на Здравко: `Encorp HW W05-01 Orders Processor - Logs`, с трите таба и заглавия на колоните. Здравко избира документа в Google Sheets нодовете (credential `Google Sheets account ai-academy`); ако credential-ът е към друг Google акаунт, документът се споделя с него |
| Q4 | Търговска сфера | R7 | неблокиращ | Книжарница/канцелария (както в примера), измислени доставчици | assumed | |
| Q5 | RAG: Supabase pgvector (съществуващият проект и Gemini embeddings, както в 18 и 20), нова таблица `suppliers` | R7 | неблокиращ | Да, с малък ingest workflow за ~10 измислени доставчика (два "Димитър", един с груба грешка в името) | assumed | |
| Q6 | Как се гарантира "само при изрично потвърждение" | R5 | неблокиращ | Chat нод Send and Wait с бутони; изпращането зависи само от бутона, не от преценка на LLM | assumed | |
| Q7 | Тестови получатели: доставчиците са измислени, а имейлът реално се праща | R15 | неблокиращ | Edit Fields - Run Settings нод с `testRecipientOverride`, който Здравко попълва със собствен адрес за тестове | assumed | |
| Q8 | Модел | R2 | неблокиращ | OpenRouter `openai/gpt-4o-mini` (поддържа снимки), temperature 0.3 | assumed | |
| Q9 | Jailbreak механизъм | R13, R14 | неблокиращ | Guardrails нод (jailbreak) на входа и на изхода на агента, плюс правила в system prompt; при засичане: спира се, Chat нод с отказ, ред в `jailbreak_log` | assumed | |
| Q10 | Известие за грешка | R11 | неблокиращ | Error workflow: ред в `error_log` и Telegram съобщение (Chat нодът не може да пише извън чат сесия) | assumed | |
| Q11 | Повторна обработка при празен изход: Error workflow върви в отделен run и не може да върне отговор в чат сесията | R11, R12 | неблокиращ | В същия run: празен изход -> съобщението се подава пак на агента (до 2 пъти) с Chat нод "опитвам отново"; ако пак е празен -> Chat нод със съобщение за грешка -> Stop and Error с контекста; Error workflow логва и известява | assumed | |
| Q12 | Памет на агента | R2, R5 | неблокиращ | Postgres Chat Memory (persistent), ключ `sessionId + executionId` | answered | Здравко: persistent памет, която не се губи при рестарт (2026-10-29) |
| Q13 | Code нод за разделяне на снимките | R3 | неблокиращ | Един Code нод, останалото native | answered | Прието (2026-10-29) |
| Q14 | Снимки и артикули | R3, R9 | неблокиращ | Няколко снимки и няколко артикула в една поръчка; снимките само в първото съобщение; по един ред на артикул в `purchase_orders` | answered | Заявено от Здравко (2026-10-29) |
| Q15 | Източник на доставчиците | R7 | неблокиращ | Google Sheet таб `suppliers` -> Suppliers Sync | answered | Заявено от Здравко (2026-10-29). Обновено 2026-10-30: промените (нови, редактирани, изтрити редове) се засичат с хеш на целия таб на всеки 5 минути, вместо Sheets Trigger |
| Q16 | Jailbreak защита | R13, R14 | неблокиращ | Отделен MCP сървър (Guard), вика се детерминирано от MCP Client нод на вход и изход | answered | Избрано от Здравко (2026-10-29) |
| Q17 | Дати и ден от седмицата | R8-R10 | неблокиращ | Моделът връща `delivery_when`, датата се смята детерминирано с Luxon (Europe/Sofia) | answered | Заявено от Здравко (2026-10-30), след проблем с "следващия понеделник" |
| Q18 | Тестване | всички | неблокиращ | Нативни n8n Evaluations (Data Table `orders_eval_dataset`) и Eval Runner с резултат в таб `eval_results` | answered | Заявено от Здравко (2026-10-30); 16/16 успешни |
