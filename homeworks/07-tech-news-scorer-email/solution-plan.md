# 07-tech-news-scorer-email - Оценка и верификация на tech новини

- Статус: `submitted`
- Версия: v1
- Файл: `n8n-workflows/07-tech-news-scorer-email.json` (n8n 2.41.6)

> Този документ е изграден при миграцията от реалния workflow. Обосновката на избора на нодове, допусканията, тестовият план и покритието R -> нод не са запазени - допълни ги.

## Изисквания R1..Rn

_(липсват - виж `assignment.md`)_

## Схема на потока (връзки)

```
RSS Feed Trigger -> AI Agent - tech news scorer
OpenRouter Chat Model -> AI Agent - tech news scorer [ai_languageModel]
Structured Output Parser -> AI Agent - tech news scorer [ai_outputParser]
AI Agent - tech news scorer -> If score > 7
If score > 7 -> AI Agent - Article verifier
Structured Output Parser1 -> AI Agent - Article verifier [ai_outputParser]
OpenRouter Chat Model1 -> AI Agent - Article verifier [ai_languageModel]
HTTP Request -> AI Agent - Article verifier [ai_tool]
AI Agent - Article verifier -> AI Agent - email content writer
OpenRouter Chat Model2 -> AI Agent - email content writer [ai_languageModel]
Structured Output Parser2 -> AI Agent - email content writer [ai_outputParser]
AI Agent - email content writer -> Send a message
```

## Нодове

| № | Нод | Тип | Роля | Ключови параметри |
|---|-----|-----|------|-------------------|
| 1 | RSS Feed Trigger | `rssFeedReadTrigger` v1 | Тригер при нов RSS запис | `feedUrl`: https://www.theverge.com/rss/tech/index.xml |
| 2 | OpenRouter Chat Model | `lmChatOpenRouter` v1 | Chat модел (OpenRouter) |  |
| 3 | Structured Output Parser | `outputParserStructured` v1.3 | Структуриран изход за агента |  |
| 4 | AI Agent - tech news scorer | `agent` v3.1 | AI Agent | `text`: =Rate the importance of this tech news from 1 (trivial) to 10 (industry-changing |
| 5 | If score > 7 | `if` v2.3 | Условно разклонение | `conditions`: {"options": {"caseSensitive": true, "leftValue": "", "typeValidation": "strict", |
| 6 | AI Agent - Article verifier | `agent` v3.1 | AI Agent | `text`: =Verify this story using at least 2 independent sources other than The Verge by  |
| 7 | Structured Output Parser1 | `outputParserStructured` v1.3 | Структуриран изход за агента |  |
| 8 | OpenRouter Chat Model1 | `lmChatOpenRouter` v1 | Chat модел (OpenRouter) |  |
| 9 | HTTP Request | `httpRequestTool` v4.5 | HTTP заявка като tool на AI агент | `url`: https://serpapi.com/search?engine=google |
| 10 | OpenRouter Chat Model2 | `lmChatOpenRouter` v1 | Chat модел (OpenRouter) |  |
| 11 | Structured Output Parser2 | `outputParserStructured` v1.3 | Структуриран изход за агента |  |
| 12 | AI Agent - email content writer | `agent` v3.1 | AI Agent | `text`: =  Write a news article (about 400 words) with a headline, based ONLY on the fac |
| 13 | Send a message | `gmail` v2.2 | Изпраща имейл (Gmail) |  |

## Credentials (само типове и имена)

- `gmailOAuth2` (Gmail account)
- `openRouterApi` (OpenRouter account)
- `serpApi` (SerpAPI account)

## Допускания

_(липсват)_

## Тестов план

_(липсва)_

## Покритие R -> нод

_(липсва)_
