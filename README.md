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

Статуси: `received` -> `plan-proposed` -> `plan-approved` -> `json-delivered` -> `tested` -> `submitted` -> `graded`.

## Структура

- `n8n-workflows/` - последната версия на всяко решение (`NN-slug.json`), предишни версии в `_versions/`
- `homeworks/NN-slug/` - условие, план, changelog, тестови данни, скриншоти (по желание), обратна връзка
- `knowledge/` - модели, поуки, потвърдени `typeVersion`
- `tools/validate_workflow.py` - валидатор и санитизатор на експорти (`--sanitize`)
