# 06-github-issues-summary - Резюме на GitHub issues с AI

- Статус: `submitted`
- Версия: v1
- Файл: `n8n-workflows/06-github-issues-summary.json` (n8n 2.41.6)

> Този документ е изграден при миграцията от реалния workflow. Обосновката на избора на нодове, допусканията, тестовият план и покритието R -> нод не са запазени - допълни ги.

## Изисквания R1..Rn

_(липсват - виж `assignment.md`)_

## Схема на потока (връзки)

```
Every morning at 6 am -> Get issues of a repository
When clicking ‘Execute workflow’ -> Get issues of a repository
Get issues of a repository -> Edit Fields
Edit Fields -> AI Agent - Summarize issues
Structured Output Parser -> AI Agent - Summarize issues [ai_outputParser]
OpenRouter Chat Model -> AI Agent - Summarize issues [ai_languageModel]
AI Agent - Summarize issues -> Code in JavaScript
AI Agent - Summarize issues -> If security issue detected
OpenRouter Chat Model1 -> AI Agent - Email message composer [ai_languageModel]
AI Agent - Email message composer -> Send a message
Code in JavaScript -> AI Agent - Email message composer
If security issue detected -> Send a rich message
```

## Нодове

| № | Нод | Тип | Роля | Ключови параметри |
|---|-----|-----|------|-------------------|
| 1 | When clicking ‘Execute workflow’ | `manualTrigger` v1 | Ръчно стартиране за тест |  |
| 2 | Every morning at 6 am | `scheduleTrigger` v1.4 | Стартира потока по график | `rule`: {"interval": [{"triggerAtHour": 6}]} |
| 3 | Get issues of a repository | `github` v1.1 | GitHub API | `resource`: repository |
| 4 | Edit Fields | `set` v3.5 | Задава/трансформира полета |  |
| 5 | Structured Output Parser | `outputParserStructured` v1.3 | Структуриран изход за агента |  |
| 6 | OpenRouter Chat Model | `lmChatOpenRouter` v1 | Chat модел (OpenRouter) |  |
| 7 | Send a message | `gmail` v2.2 | Изпраща имейл (Gmail) |  |
| 8 | AI Agent - Summarize issues | `agent` v3.1 | AI Agent | `text`: =Make summary of the issue that is provided: <issue-url>{{$json.url}}</issue-url |
| 9 | OpenRouter Chat Model1 | `lmChatOpenRouter` v1 | Chat модел (OpenRouter) |  |
| 10 | AI Agent - Email message composer | `agent` v3.1 | AI Agent | `text`: =This is the issue digest: {{ $json.text }} |
| 11 | Code in JavaScript | `code` v2 | Код (JavaScript) |  |
| 12 | Send a rich message | `telegram` v1.2 | Изпраща съобщение в Telegram | `operation`: sendRichMessage |
| 13 | If security issue detected | `if` v2.3 | Условно разклонение | `conditions`: {"options": {"caseSensitive": true, "leftValue": "", "typeValidation": "loose",  |

## Credentials (само типове и имена)

- `githubApi` (GitHub account)
- `gmailOAuth2` (Gmail account)
- `openRouterApi` (OpenRouter account)
- `telegramApi` (Telegram account)

## Допускания

_(липсват)_

## Тестов план

_(липсва)_

## Покритие R -> нод

_(липсва)_
