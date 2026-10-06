# 02-cat-fact-daily-email - Ежедневен факт за котки по имейл (AI)

- Статус: `json-delivered`
- Версия: v1
- Файл: `n8n-workflows/02-cat-fact-daily-email.json` (n8n 2.41.6)

> Този документ е изграден при миграцията от реалния workflow. Обосновката на избора на нодове, допусканията, тестовият план и покритието R -> нод не са запазени - допълни ги.

## Изисквания R1..Rn

_(липсват - виж `assignment.md`)_

## Схема на потока (връзки)

```
When clicking ‘Execute workflow’ -> HTTP Request
Every day at 8:36 am -> HTTP Request
HTTP Request -> AI Agent
OpenRouter Chat Model -> AI Agent [ai_languageModel]
AI Agent -> Send a message
```

## Нодове

| № | Нод | Тип | Роля | Ключови параметри |
|---|-----|-----|------|-------------------|
| 1 | When clicking ‘Execute workflow’ | `manualTrigger` v1 | Ръчно стартиране за тест |  |
| 2 | Every day at 8:36 am | `scheduleTrigger` v1.3 | Стартира потока по график | `rule`: {"interval": [{"triggerAtHour": 8, "triggerAtMinute": 36}]} |
| 3 | HTTP Request | `httpRequest` v4.4 | HTTP заявка към външен API | `url`: https://catfact.ninja/fact |
| 4 | OpenRouter Chat Model | `lmChatOpenRouter` v1 | Chat модел (OpenRouter) |  |
| 5 | AI Agent | `agent` v3.1 | AI Agent | `text`: =Направи разширено проучване за да обогатиш и разшириш с още интересни факти и и |
| 6 | Send a message | `gmail` v2.2 | Изпраща имейл (Gmail) |  |

## Credentials (само типове и имена)

- `gmailOAuth2` (Gmail account)
- `openRouterApi` (OpenRouter account)

## Допускания

_(липсват)_

## Тестов план

_(липсва)_

## Покритие R -> нод

_(липсва)_
