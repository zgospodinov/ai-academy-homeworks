# 05-form-ip-geolocation - Форма с IP геолокация

- Статус: `submitted`
- Версия: v1
- Файл: `n8n-workflows/05-form-ip-geolocation.json` (n8n 2.41.6)

> Този документ е изграден при миграцията от реалния workflow. Обосновката на избора на нодове, допусканията, тестовият план и покритието R -> нод не са запазени - допълни ги.

## Изисквания R1..Rn

_(липсват - виж `assignment.md`)_

## Схема на потока (връзки)

```
Webhook -> Respond to Webhook
Webhook (POST) -> Respond to Webhook1
Edit Fields (IP) -> HTTP Request (ipwho.is)
HTTP Request (ipwho.is) -> IF lookup ok
IF lookup ok -> Edit Fields (normalize) (изход 0)
IF lookup ok -> Log lookup failure (изход 1)
Edit Fields (normalize) -> Log submission
Log submission -> IF is_eu
IF is_eu -> EU branch (изход 0)
IF is_eu -> Non-EU branch (изход 1)
EU branch -> IF mismatch
Non-EU branch -> IF mismatch
IF mismatch -> Flag + notify (изход 0)
IF mismatch -> No action (изход 1)
Respond to Webhook1 -> Edit Fields (IP)
```

## Нодове

| № | Нод | Тип | Роля | Ключови параметри |
|---|-----|-----|------|-------------------|
| 1 | Webhook | `webhook` v2.1 | Приема HTTP заявка | `path`: user-form |
| 2 | Respond to Webhook | `respondToWebhook` v1.5 | Връща отговор на webhook-а |  |
| 3 | Webhook (POST) | `webhook` v2 | Приема HTTP заявка | `path`: user-form |
| 4 | Edit Fields (IP) | `set` v3.4 | Задава/трансформира полета |  |
| 5 | HTTP Request (ipwho.is) | `httpRequest` v4.2 | HTTP заявка към външен API | `url`: ={{ 'https://ipwho.is/' + (/^(10\.\|192\.168\.\|172\.(1[6-9]\|2\d\|3[01])\.\|127 |
| 6 | IF lookup ok | `if` v2.2 | Условно разклонение | `conditions`: {"options": {"caseSensitive": true, "leftValue": "", "typeValidation": "strict", |
| 7 | Log lookup failure | `set` v3.4 | Задава/трансформира полета |  |
| 8 | Edit Fields (normalize) | `set` v3.4 | Задава/трансформира полета |  |
| 9 | Log submission | `noOp` v1 | Без действие (маркер на клон) |  |
| 10 | IF is_eu | `if` v2.2 | Условно разклонение | `conditions`: {"options": {"caseSensitive": true, "leftValue": "", "typeValidation": "loose",  |
| 11 | EU branch | `set` v3.4 | Задава/трансформира полета |  |
| 12 | Non-EU branch | `set` v3.4 | Задава/трансформира полета |  |
| 13 | IF mismatch | `if` v2.2 | Условно разклонение | `conditions`: {"options": {"caseSensitive": true, "leftValue": "", "typeValidation": "loose",  |
| 14 | Flag + notify | `set` v3.4 | Задава/трансформира полета |  |
| 15 | No action | `noOp` v1 | Без действие (маркер на клон) |  |
| 16 | Respond to Webhook1 | `respondToWebhook` v1.1 | Връща отговор на webhook-а |  |

## Credentials (само типове и имена)

- няма

## Бележки от Sticky Notes

> ## Flow B: process the submission
> 
> Receives the POST from the HTML form (Flow A serves the form on the same path with a GET webhook).

> ## Flow A: Serve the web form
> 
> Workaround for this task given n8n is hosted on local machine

## Допускания

_(липсват)_

## Тестов план

_(липсва)_

## Покритие R -> нод

_(липсва)_
