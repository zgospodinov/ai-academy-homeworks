# 03-hn-n8n-telegram-digest - Hacker News дайджест в Telegram

- Статус: `submitted`
- Версия: v1
- Файл: `n8n-workflows/03-hn-n8n-telegram-digest.json` (n8n 2.41.6)

> Този документ е изграден при миграцията от реалния workflow. Обосновката на избора на нодове, допусканията, тестовият план и покритието R -> нод не са запазени - допълни ги.

## Изисквания R1..Rn

_(липсват - виж `assignment.md`)_

## Схема на потока (връзки)

```
When clicking ‘Execute workflow’ -> HTTP Request
Schedule Trigger -> HTTP Request
HTTP Request -> Split Out
Split Out -> Edit Fields
Edit Fields -> Aggregate
Aggregate -> Code in JavaScript
Code in JavaScript -> Send a text message
```

## Нодове

| № | Нод | Тип | Роля | Ключови параметри |
|---|-----|-----|------|-------------------|
| 1 | When clicking ‘Execute workflow’ | `manualTrigger` v1 | Ръчно стартиране за тест |  |
| 2 | Schedule Trigger | `scheduleTrigger` v1.3 | Стартира потока по график | `rule`: {"interval": [{"field": "weeks"}]} |
| 3 | HTTP Request | `httpRequest` v4.4 | HTTP заявка към външен API | `url`: https://hn.algolia.com/api/v1/search?query=n8n |
| 4 | Split Out | `splitOut` v1 | Разделя масив на елементи |  |
| 5 | Edit Fields | `set` v3.4 | Задава/трансформира полета |  |
| 6 | Send a text message | `telegram` v1.2 | Изпраща съобщение в Telegram | `chatId`: -5531928417 |
| 7 | Aggregate | `aggregate` v1 | Събира елементи в един |  |
| 8 | Code in JavaScript | `code` v2 | Код (JavaScript) |  |

## Credentials (само типове и имена)

- `telegramApi` (Telegram account)

## Допускания

_(липсват)_

## Тестов план

_(липсва)_

## Покритие R -> нод

_(липсва)_
