# Solution plan - 12-support-ticket-router

- Статус: `tested` (одобрен план v1 2026-10-15; v2 по решение на Здравко 2026-10-16; JSON доставен 2026-10-16; Здравко пусна всички сценарии от `test-data/test-tickets.md` на 2026-10-16 - работи правилно, без проблеми)
- Версия: v2 (v1 с два workflow-а и Data Table е архивиран в `n8n-workflows/_versions/12-support-ticket-router/`)
- Workflow име: `Encorp | Homework | Week 03 | HW 05 | Support Ticket Router` (`n8n-workflows/12-support-ticket-router.json`)
- Таг: `encorp-homework`

## Изисквания
R1..R7 са в `assignment.md`. Добавено от Здравко (не е от условието):
- Каналът за ревюто е Gmail.
- Оригиналът на категорията се пази и се знае кога какво е променено: втори таб `Audit Log` в същия spreadsheet.
- v2: ЕДИН workflow с вградения Gmail Send and Wait (Custom Form). Допускане: обемът на тикетите е малък, затова простият дизайн е достатъчен.
- Workflow 3 (проверка на статусите и напомняне) и преходът към дизайна от v1 са описани само в Sticky Note.

## Схема
```
Ticket Form -> Prepare Ticket -> Analyze Urgency (Sentiment, 4 изхода) -> Classify Department (4 + Other)
  -> Department Sales / Technical / Billing / General (Other -> General) -> Build Ticket Record
  -> Compose Review Message (Code) -> Request Sentiment Review (Gmail Send and Wait, Custom Form; изпълнението е в "Waiting")
  -> Read Review Decision (Set) -> Apply Review (Set) -> Log Review To Audit Sheet (Sheets Append)
  -> Support Agent (ai_languageModel: Agent Chat Model; ai_tool: Append Ticket To Sheet, Create Google Task)
```
OpenRouter Chat Model е общ за Analyze Urgency и Classify Department.

## Нодове
| № | Нод | Защо | Ключови параметри | Покрива |
|---|-----|------|-------------------|---------|
| 1 | Ticket Form (Form Trigger 2.3) | вход на тикети, лесен ръчен тест | `Customer name`, `Ticket text` (задължително), path `support-ticket` | R1 |
| 2 | Prepare Ticket (Set) | единен вид, ticketId, `reviewerEmail` | ticketId = `TCK-` + дата + случаен суфикс | R1 |
| 3 | Analyze Urgency (Sentiment Analysis 1.1) | спешност | `Urgent, Frustrated, Neutral, Positive`, собствен System Prompt, Retry 3 | R2 |
| 4 | Classify Department (Text Classifier 1.1) | отдел | `Sales, Technical, Billing, General`, fallback Other, собствен System Prompt | R3 |
| 5 | 4x Department * (Set) | класификаторът не записва категорията в item-а; Other -> General | `department` | R3 |
| 6 | Build Ticket Record (Set) | фиксира `sentimentAi` | | R4 |
| 7 | Compose Review Message (Code) | тема и HTML със escape-нат текст на клиента | | R4 |
| 8 | Request Sentiment Review (Gmail 2.2, Send and Wait) | човекът потвърждава или сменя | Custom Form: dropdown `Sentiment category` (задължително), `Reviewer note`; без Limit Wait Time | R4 |
| 9 | Read Review Decision (Set) | чете избраната категория от `data` | по етикет на полето, иначе по стойност; резерв: AI категорията | R4 |
| 10 | Apply Review (Set) | промяната в данните на тикета | `sentimentOriginal`, `sentiment` (крайна), `sentimentChanged`, `reviewerNote`, `reviewedAt`, `processingDate` | R4 |
| 11 | Log Review To Audit Sheet (Google Sheets Append) | история: оригинал, крайна, променена ли е | таб `Audit Log`, Cell Format RAW | добра практика |
| 12 | Support Agent (AI Agent 3.1) | отговор + двата tool-а | System Prompt: еднократно извикване на tool-овете | R5 |
| 13 | Append Ticket To Sheet (Google Sheets Tool) | ред в таб `Tickets` | дата, текст, категория, отдел с expressions; само отговорът е `$fromAI`; RAW | R6 |
| 14 | Create Google Task (Google Tasks Tool) | задача | `title` и `notes` с `$fromAI`; списък `@default` | R7 |

Sticky Notes: общо описание (какво е променено и защо), "Design considerations, alternatives and recommendations", 4 групови бележки (Intake, AI класификация, Human in the Loop, Agent и tools).

## Допускания и credentials
- Credentials (само имена): OpenRouter, Gmail, Google Sheets OAuth2, Google Tasks OAuth2 (Google Tasks API включен в Google Cloud проекта).
- Spreadsheet с табове `Tickets` и `Audit Log` (заглавия в `test-data/sheet-header-*.csv`); `YOUR_SPREADSHEET_ID` се сменя в трите Sheets нода.
- `reviewerEmail` в Prepare Ticket се сменя с адреса на ревюиращия.
- Линкът в имейла идва от `WEBHOOK_URL` на инстанцията и трябва да се отваря от браузъра на ревюиращия.
- Агентът отговаря на езика на тикета; заглавието и бележките на задачата са на английски.

## Потвърдено с тест (Здравко, 2026-10-16)
Всички сценарии от `test-data/test-tickets.md` минават без проблеми. Това потвърждава: Gmail Send and Wait с `customForm`; нодовете `googleSheetsTool` (4.7) и `googleTasksTool` (1) с `task: "@default"`; `$('Apply Review')` в tool нодовете; `appendAttribution: false`; смяната и потвържденията на категорията в `Tickets` и `Audit Log`; паралелно чакащи тикети.

## Остава непроверено
- Кой точно е ключът в изхода на Custom Form (етикет или име на полето) - Read Review Decision работи и в двата случая (резерв по стойност), точният ключ не е записан.
- Дали pruning премахва изчакващи изпълнения (описано в Sticky Note като риск).
- Дизайнът на v1 (два workflow-а и Data Table) не е тестван; архивиран е само като алтернатива.

## Доказателства от теста (screenshots)
Снимките са на Здравко от теста на 2026-10-16 (оригинални, непроменени; Здравко се е погрижил да няма конфиденциални данни):
- `screenshots/review-01-inbox.png` - входящата поща с имейла за ревю (`[Review needed] <ticketId> - AI: Urgent / Technical`).
- `screenshots/review-02-email.png` - съдържанието на имейла: ticket id, клиент, отдел, AI категория, текст и бутон "Open review form".
- `screenshots/review-03-form.png` - Custom Form на Send and Wait: dropdown `Sentiment category` и `Reviewer note`.
- `screenshots/review-04-google-tasks.png` - Google Tasks със създадените задачи в списъка за тикетите (`[Department] ...`, ticket id и категория в бележките).
Липсват снимки на Executions/канвас и на таба `Tickets` и `Audit Log`; добави ги при предаване, ако се изискват.

## Тестов план
Виж `test-data/test-tickets.md`.

## Покритие
R1 -> 1-2 · R2 -> 3 · R3 -> 4-5 · R4 -> 6-11 · R5 -> 12 · R6 -> 13 · R7 -> 14.
