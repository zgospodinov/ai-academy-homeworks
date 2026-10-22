# AI Academy homeworks (Encorp 2026)

Решения на домашни от Encorp AI Academy с n8n (self-hosted n8n 2.41.6). Структурата и правилата са описани в skill-а `n8n-academy-homeworks`.

## Индекс

| № | Седмица | Домашно | Статус | Версия | Файл | Ключови нодове | Обновено |
|---|---------|---------|--------|--------|------|----------------|----------|
| 01 | 1 | Прогноза за времето: филтриране и обединяване | submitted | v1 | `n8n-workflows/01-weather-data-filter-merge.json` | code, filter, merge, openWeatherMap, renameKeys | 2026-10-06 |
| 02 | 1 | Ежедневен факт за котки по имейл (AI) | submitted | v1 | `n8n-workflows/02-cat-fact-daily-email.json` | agent, gmail, httpRequest, lmChatOpenRouter, scheduleTrigger | 2026-10-06 |
| 03 | 1 | Hacker News дайджест в Telegram | submitted | v1 | `n8n-workflows/03-hn-n8n-telegram-digest.json` | aggregate, code, httpRequest, scheduleTrigger, set, splitOut, telegram | 2026-10-06 |
| 04 | 1 | Мониторинг на достъпност на услуги | submitted | v1 | `n8n-workflows/04-service-uptime-monitor.json` | code, gmail, httpRequest, if, scheduleTrigger | 2026-10-06 |
| 05 | 1 | Форма с IP геолокация | submitted | v1 | `n8n-workflows/05-form-ip-geolocation.json` | httpRequest, if, noOp, respondToWebhook, set, webhook | 2026-10-06 |
| 06 | 1 | Резюме на GitHub issues с AI | submitted | v1 | `n8n-workflows/06-github-issues-summary.json` | agent, code, github, gmail, if, lmChatOpenRouter, outputParserStructured, scheduleTrigger, set, telegram | 2026-10-06 |
| 07 | 1 | Оценка и верификация на tech новини | submitted | v1 | `n8n-workflows/07-tech-news-scorer-email.json` | agent, gmail, httpRequestTool, if, lmChatOpenRouter, outputParserStructured, rssFeedReadTrigger | 2026-10-06 |
| 08 | 3 | Анализ на настроенията в обратна връзка от клиенти | tested | v3 | `n8n-workflows/08-customer-feedback-sentiment.json` | sentimentAnalysis, lmChatOpenRouter, aggregate, set, filter, code, gmail | 2026-10-13 |
| 09 | 3 | Скрининг на кандидати за работа (Form + Information Extractor) | tested | v3 | `n8n-workflows/09-job-application-screening.json` | formTrigger, informationExtractor, code, if, chainLlm, outputParserStructured, googleSheets | 2026-10-13 |
| 10 | 3 | Smart Content Categorizer (Webhook + Text Classifier + Data Table) | tested | v3 | `n8n-workflows/10-smart-content-categorizer.json` (+ `-reject-article`, `-error-handler`) | webhook, respondToWebhook, splitOut, textClassifier, set, merge, dataTable, aggregate, executeWorkflow, stopAndError, errorTrigger, telegram | 2026-10-14 |
| 11 | 3 | Резюме на сутрешни срещи (Summarization Chain: Map Reduce / Refine / Stuff) | tested | v2 | `n8n-workflows/11-meeting-notes-summariser.json` | scheduleTrigger, code, chainSummarization, lmChatOpenRouter, dateTime, set, aggregate, if, merge | 2026-10-14 |
| 12 | 3 | Support Ticket Router with Human Support (Sentiment + Text Classifier + Gmail Send and Wait + AI Agent) | tested | v2 | `n8n-workflows/12-support-ticket-router.json` | formTrigger, sentimentAnalysis, textClassifier, gmail (sendAndWait), agent, googleSheets, googleSheetsTool, googleTasksTool | 2026-10-16 |
| 13 | 3 | Expense Receipt Assistant (Form + vision Basic LLM Chain + Data Tables + Send and Wait; бонуси: отчет, чат агент, error alert) | tested | v2 | `n8n-workflows/13-expense-receipt-assistant.json` (+ `-weekly-report`, `-chat-agent`, `-spending-lookup`, `-error-alert`) | formTrigger, chainLlm, outputParserStructured, dataTable, switch, gmail (sendAndWait), summarize, toolWorkflow | 2026-10-16 |
| 14 | 4 | Token Counter (Form Trigger + Gemini/OpenAI Message a Model + Google Sheets, токени и цена) | tested | v1 | `n8n-workflows/14-token-counter.json` | formTrigger, switch, openAi, googleGemini, set, code, googleSheets | 2026-10-22 |
| 15 | 4 | The Fact-Finding Agent (AI Agent + Calculator + Wikipedia tool) | tested | v2 | `n8n-workflows/15-fact-finding-agent.json` | chatTrigger, agent, lmChatOpenRouter, toolCalculator, toolWikipedia | 2026-10-22 |

Статуси: `received` -> `plan-proposed` -> `plan-approved` -> `json-delivered` -> `tested` -> `submitted` -> `graded`.

## Структура

- `n8n-workflows/` - последната версия на всяко решение (`NN-slug.json`), предишни версии в `_versions/`
- `homeworks/NN-slug/` - условие, план, changelog, тестови данни, скриншоти (по желание), обратна връзка
- `knowledge/` - модели, поуки, потвърдени `typeVersion`
- `tools/validate_workflow.py` - валидатор и санитизатор на експорти (`--sanitize`)
| 16 | 4 | Long-Term Memory Agent (AI Agent + Postgres Chat Memory + Supabase, памет по session_id) | tested | v1 | `n8n-workflows/16-long-term-memory-agent.json` | chatTrigger, agent, lmChatOpenRouter, memoryPostgresChat | 2026-10-22 |
