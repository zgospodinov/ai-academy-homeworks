# 04-service-uptime-monitor - Мониторинг на достъпност на услуги

- Статус: `json-delivered`
- Версия: v1
- Файл: `n8n-workflows/04-service-uptime-monitor.json` (n8n 2.41.6)

> Този документ е изграден при миграцията от реалния workflow. Обосновката на избора на нодове, допусканията, тестовият план и покритието R -> нод не са запазени - допълни ги.

## Изисквания R1..Rn

_(липсват - виж `assignment.md`)_

## Схема на потока (връзки)

```
When clicking ‘Execute workflow’ -> Seed list of services to monitor
Once a day at 5am -> Seed list of services to monitor
Seed list of services to monitor -> HTTP Request
HTTP Request -> If http status code != 200
If http status code != 200 -> Send a message
```

## Нодове

| № | Нод | Тип | Роля | Ключови параметри |
|---|-----|-----|------|-------------------|
| 1 | When clicking ‘Execute workflow’ | `manualTrigger` v1 | Ръчно стартиране за тест |  |
| 2 | Seed list of services to monitor | `code` v2 | Код (JavaScript) |  |
| 3 | Once a day at 5am | `scheduleTrigger` v1.3 | Стартира потока по график | `rule`: {"interval": [{"triggerAtHour": 5}]} |
| 4 | HTTP Request | `httpRequest` v4.4 | HTTP заявка към външен API | `url`: ={{ $json.service }} |
| 5 | Send a message | `gmail` v2.2 | Изпраща имейл (Gmail) |  |
| 6 | If http status code != 200 | `if` v2.3 | Условно разклонение | `conditions`: {"options": {"caseSensitive": true, "leftValue": "", "typeValidation": "strict", |

## Credentials (само типове и имена)

- `gmailOAuth2` (Gmail account)

## Допускания

_(липсват)_

## Тестов план

_(липсва)_

## Покритие R -> нод

_(липсва)_
