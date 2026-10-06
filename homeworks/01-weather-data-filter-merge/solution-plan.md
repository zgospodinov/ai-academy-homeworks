# 01-weather-data-filter-merge - Прогноза за времето: филтриране и обединяване

- Статус: `json-delivered`
- Версия: v1
- Файл: `n8n-workflows/01-weather-data-filter-merge.json` (n8n 2.41.6)

> Този документ е изграден при миграцията от реалния workflow. Обосновката на избора на нодове, допусканията, тестовият план и покритието R -> нод не са запазени - допълни ги.

## Изисквания R1..Rn

_(липсват - виж `assignment.md`)_

## Схема на потока (връзки)

```
start workflow -> seed data hardcoded with temperatures (AI generated)
start workflow -> seed data from lesson 1
seed data hardcoded with temperatures (AI generated) -> get cities with temp < 15
get cities with temp < 15 -> return humidity or windspeed based on city population
seed data from lesson 1 -> OpenWeatherMap
seed data from lesson 1 -> Rename merge key
OpenWeatherMap -> Merge by city name
Rename merge key -> Merge by city name
get cities with temp <  -> return humidity or windspeed based on city population2
Merge by city name -> get cities with temp < 
```

## Нодове

| № | Нод | Тип | Роля | Ключови параметри |
|---|-----|-----|------|-------------------|
| 1 | start workflow | `manualTrigger` v1 | Ръчно стартиране за тест |  |
| 2 | OpenWeatherMap | `openWeatherMap` v1 | Данни за времето (OpenWeatherMap) |  |
| 3 | seed data hardcoded with temperatures (AI generated) | `code` v2 | Код (JavaScript) |  |
| 4 | get cities with temp < 15 | `filter` v2.3 | Филтрира елементи | `conditions`: {"options": {"caseSensitive": true, "leftValue": "", "typeValidation": "strict", |
| 5 | seed data from lesson 1 | `code` v2 | Код (JavaScript) |  |
| 6 | return humidity or windspeed based on city population | `code` v2 | Код (JavaScript) |  |
| 7 | Rename merge key | `renameKeys` v1 | Преименува ключове |  |
| 8 | return humidity or windspeed based on city population2 | `code` v2 | Код (JavaScript) |  |
| 9 | get cities with temp <  | `filter` v2.3 | Филтрира елементи | `conditions`: {"options": {"caseSensitive": true, "leftValue": "", "typeValidation": "strict", |
| 10 | Merge by city name | `merge` v3.2 | Обединява потоци |  |

## Credentials (само типове и имена)

- `openWeatherMapApi` (OpenWeatherMap account)

## Бележки от Sticky Notes

> ## Static weather forecast data Workflow

> ## Dynamic weather forecast data Workflow

## Допускания

_(липсват)_

## Тестов план

_(липсва)_

## Покритие R -> нод

_(липсва)_
