# typeVersion в експортите (n8n 2.41.6)

Източник: реалните експорти на Здравко в `n8n-workflows/` (миграция 2026-10-06). Версиите, използвани в работещи експорти, са доказателство, че се импортират. Допълвай при нови потвърдени импорти.

| Нод (тип) | typeVersion | Домашни |
|-----------|-------------|---------|
| `@n8n/n8n-nodes-langchain.agent` | 3.1 | 02, 06, 07 |
| `@n8n/n8n-nodes-langchain.lmChatOpenRouter` | 1 | 02, 06, 07, 08 |
| `@n8n/n8n-nodes-langchain.sentimentAnalysis` | 1.1 | 08 (потвърдено с изпълнение) |
| `@n8n/n8n-nodes-langchain.outputParserStructured` | 1.3 | 06, 07 |
| `n8n-nodes-base.aggregate` | 1 | 03, 08 |
| `n8n-nodes-base.code` | 2 | 01, 03, 04, 06, 08 |
| `n8n-nodes-base.filter` | 2.3 | 01, 08 |
| `n8n-nodes-base.github` | 1.1 | 06 |
| `n8n-nodes-base.gmail` | 2.2 | 02, 04, 06, 07, 08 |
| `n8n-nodes-base.httpRequest` | 4.2 | 05 |
| `n8n-nodes-base.httpRequest` | 4.4 | 02, 03, 04 |
| `n8n-nodes-base.httpRequestTool` | 4.5 | 07 |
| `n8n-nodes-base.if` | 2.2 | 05 |
| `n8n-nodes-base.if` | 2.3 | 04, 06, 07 |
| `n8n-nodes-base.manualTrigger` | 1 | 01, 02, 03, 04, 06, 08 |
| `n8n-nodes-base.merge` | 3.2 | 01, 08 |
| `n8n-nodes-base.noOp` | 1 | 05, 08 |
| `n8n-nodes-base.openWeatherMap` | 1 | 01 |
| `n8n-nodes-base.renameKeys` | 1 | 01 |
| `n8n-nodes-base.respondToWebhook` | 1.1 | 05 |
| `n8n-nodes-base.respondToWebhook` | 1.5 | 05 |
| `n8n-nodes-base.rssFeedReadTrigger` | 1 | 07 |
| `n8n-nodes-base.scheduleTrigger` | 1.3 | 02, 03, 04 |
| `n8n-nodes-base.scheduleTrigger` | 1.4 | 06 |
| `n8n-nodes-base.set` | 3.4 | 03, 05 |
| `n8n-nodes-base.set` | 3.5 | 06, 08 |
| `n8n-nodes-base.splitOut` | 1 | 03 |
| `n8n-nodes-base.stickyNote` | 1 | 01, 05 |
| `n8n-nodes-base.telegram` | 1.2 | 03, 06 |
| `n8n-nodes-base.webhook` | 2 | 05 |
| `n8n-nodes-base.webhook` | 2.1 | 05 |
| `n8n-nodes-base.formTrigger` | 2.3 | 09 (импортирано и изпълнено) |
| `@n8n/n8n-nodes-langchain.informationExtractor` | 1.2 | 09 (импортирано и изпълнено) |
| `@n8n/n8n-nodes-langchain.chainLlm` | 1.9 | 09 (импортирано и изпълнено) |
| `n8n-nodes-base.googleSheets` | 4.7 | 09 (импортирано и изпълнено) |
| `n8n-nodes-base.executeWorkflow` | 1.2 | 09 v3 (потвърдено с изпълнение) |
| `n8n-nodes-base.executeWorkflowTrigger` | 1.1 | 09 v3 (потвърдено с изпълнение) |
| `@n8n/n8n-nodes-langchain.textClassifier` | 1.1 | 10 (импортирано и изпълнено) |
| `n8n-nodes-base.dataTable` | 1.1 | 10 (импортирано и изпълнено) |
| `n8n-nodes-base.stopAndError` | 1 | 10 (изпълнено в sub-workflow) |
| `n8n-nodes-base.errorTrigger` | 1 | 10 (изпълнено, Telegram известие) |
| `n8n-nodes-base.respondToWebhook` | 1.5 | 10 (202 и 400 отговори) |
| `n8n-nodes-base.webhook` | 2.1 | 10 |
| `n8n-nodes-base.executeWorkflow` | 1.2 | 10 (fire-and-forget към друг workflow) |
| `n8n-nodes-base.merge` | 3.2 | 10 (5 входа, потвърдено с валидни статии) |
| `@n8n/n8n-nodes-langchain.chainSummarization` | 2 | 11 (изпълнено: stuff, refine, map_reduce в бонус клона; map_reduce в главния поток, Здравко 2026-10-15) |
| `n8n-nodes-base.if` | 2.3 | 11 (изпълнено) |
| `n8n-nodes-base.merge` | 3.2 | 11 (3 входа, изпълнено) |
| `n8n-nodes-base.dateTime` | 2 | 11 (Format a Date: `operation: formatDate`, `format: custom`, `customFormat`, `outputFieldName`, `options.includeInputFields`, `options.useWorkflowTimezone` - главният поток работи по думите на Здравко) |
| `n8n-nodes-base.scheduleTrigger` | 1.4 | 11 (ръчно пускане с Execute workflow; `timestamp` се чете от Date & Time) |
| `n8n-nodes-base.formTrigger` | 2.6 | 13 (файл поле, dropdown, number; потвърдено) |
| `@n8n/n8n-nodes-langchain.chainLlm` | 1.9 | 13 (Image (Binary) съобщение + Structured Output Parser; потвърдено) |
| `n8n-nodes-base.dataTable` | 1.1 | 13 (get/insert/update по филтър; Always Output Data при липса; потвърдено) |
| `n8n-nodes-base.switch` | 3.4 | 13 (потвърдено) |
| `n8n-nodes-base.gmail` | 2.2 | 13 (send и sendAndWait с Custom Form; потвърдено) |
| `n8n-nodes-base.summarize` | 1.1 | 13 (потвърдено; суми само върху числа) |
| `@n8n/n8n-nodes-langchain.toolWorkflow` | 2.2 | 13 (Call n8n Workflow Tool; потвърдено) |
| `@n8n/n8n-nodes-langchain.chatTrigger` | 1.5 | 13 (потвърдено) |
| `@n8n/n8n-nodes-langchain.memoryBufferWindow` | 1.4 | 13 (потвърдено) |
| `n8n-nodes-base.executeWorkflowTrigger` | 1.2 | 13 (потвърдено) |

| `@n8n/n8n-nodes-langchain.openAi` (text/response, simplify off) | 2.3 | 14 (изпълнено) |
| `@n8n/n8n-nodes-langchain.googleGemini` (text/message, simplify off) | 1.2 | 14 (изпълнено) |
| `n8n-nodes-base.code` (runOnceForEachItem) | 2 | 14 (изпълнено) |
| `n8n-nodes-base.switch` | 3.4 | 14 (rules, 2 изхода) |
| `n8n-nodes-base.set` | 3.5 | 14 (изпълнено) |

| `@n8n/n8n-nodes-langchain.toolCalculator` | 1 | 15 (T1-T5 изпълнени, Здравко 2026-10-22) |
| `@n8n/n8n-nodes-langchain.toolWikipedia` | 1 | 15 (T1-T5 изпълнени) |
| `@n8n/n8n-nodes-langchain.agent` | 3.1 | 15 (Chat Trigger 1.5 + два tool-а; потвърдено) |
| `@n8n/n8n-nodes-langchain.chatTrigger` | 1.5 | 15 (потвърдено) |
| `@n8n/n8n-nodes-langchain.memoryPostgresChat` | 1.4 | 16 (T1, T2, T3, T5 изпълнени, Здравко 2026-10-22) |

| `@n8n/n8n-nodes-langchain.embeddingsGoogleGemini` | 1 | 18 (изпълнено: embedding на въпрос, модел `models/gemini-embedding-001`) |
| `@n8n/n8n-nodes-langchain.vectorStoreSupabase` (mode load) | 1.3 | 18 (изпълнено срещу празна таблица, RPC `match_manual_chunks` без грешка) |
| `@n8n/n8n-nodes-langchain.vectorStoreSupabase` (mode insert) | 1.3 | 18 (създадено през MCP, още не е изпълнено) |
| `@n8n/n8n-nodes-langchain.documentDefaultDataLoader` | 1.1 | 18 (създадено, още не е изпълнено) |
| `@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter` | 1 | 18 (създадено, още не е изпълнено) |
| `n8n-nodes-base.extractFromFile` (pdf) | 1.1 | 18 (създадено, още не е изпълнено) |
| `n8n-nodes-base.postgres` (executeQuery) | 2.7 | 18 (създадено, още не е изпълнено) |
| `n8n-nodes-base.aggregate` | 1 | 18 (създадено, още не е изпълнено) |
| `n8n-nodes-base.if` | 2.3 | 18 (създадено през MCP, още не е изпълнено) |
| `n8n-nodes-base.stopAndError` | 1 | 18 (създадено през MCP, още не е изпълнено) |
| `n8n-nodes-base.extractFromFile` (pdf) | 1.1 | 18: изпълнено, но върна празен текст (виж gotchas) |
| `n8n-nodes-base.splitInBatches` | 3 | 18 (изпълнено: batch 1, изход loop = индекс 1) |
| `n8n-nodes-base.wait` | 1.1 | 18 (изпълнено: timeInterval 65 s) |
| `n8n-nodes-base.code` (runOnceForAllItems, JavaScript) | 2 | 18 (изпълнено: сегментиране на текст) |
