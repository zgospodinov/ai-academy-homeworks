# Solution plan - 10-smart-content-categorizer

- Статус: `tested` (v3, потвърдено от Здравко 2026-10-14)
- Версия: v3 (v1 и v2 са в `n8n-workflows/_versions/10-smart-content-categorizer/`)
- Workflow имена (3 файла):
  - `Encorp | Homework | Week 03 | HW 03 | Smart Content Categorizer` (`n8n-workflows/10-smart-content-categorizer.json`)
  - `Encorp | Homework | Week 03 | HW 03 | Smart Content Categorizer Reject Article` (`...-reject-article.json`)
  - `Encorp | Homework | Week 03 | HW 03 | Smart Content Categorizer Error Handler` (`...-error-handler.json`)
- Таг: `encorp-homework`

## Изисквания
R1-R8 са в `assignment.md`. Добавено от Здравко при одобрението: webhook връща 202 и обработката е асинхронна; статистиката (не отделните статии) се записва като един ред в Data Table (за polling от външна система).

## Схема
```
Тест:    Manual Trigger -> Test Articles -> Send Test Request (POST към production webhook)

Основен: Webhook -> Validate Payload (IF)
            |- false -> Respond 400 Bad Request
            `- true  -> Respond 202 Accepted -> Split Out Articles -> Text Classifier (+ OpenRouter Chat Model)
                          |- Technology/Business/Health/Entertainment/Sports -> 5x Set (category, timestamp)
                          |      -> Merge Classified (Append, 5) -> Select Title And Text -> Aggregate Articles -> Save To Data Table
                          `- Other -> Send To Reject Article (Execute Workflow, each, без изчакване)
Reject:  When Executed by Another Workflow -> Reject As Not An Article (Stop and Error)
Error:   Error Trigger -> Format Alert -> Send Telegram Alert
```

## Нодове (основен workflow)
| № | Нод | Защо | Ключови параметри | Покрива |
|---|-----|------|-------------------|---------|
| 1 | Manual Trigger + Test Articles (Code) | Пуска теста; `SCENARIO` = mixed / valid / spam_only / invalid | 6 истински + 2 спам статии | R1 |
| 2 | Send Test Request (HTTP Request) | POST към production webhook в същия workflow | JSON `{articles: [...]}`, neverError | R1 |
| 3 | Webhook | Тригер | POST, path `smart-content-categorizer`, Respond to Webhook node | R1 |
| 4 | Validate Payload (IF) | Празен/липсващ масив -> 400 | `Array.isArray(body.articles) && length > 0` | R1 |
| 5 | Respond 202 Accepted / 400 | Fire-and-forget отговор | 202 `{status, received}` / 400 | R1 |
| 6 | Split Out Articles | Една статия = един item | Field `body.articles` | R2 |
| 7 | Text Classifier + OpenRouter Chat Model | 5 категории + Other | typeVersion 1.1, fallback `other`, multiClass off, temperature 0, собствен System Prompt Template (спам/измама/безсмислен текст -> `fallback`=true), описания "Genuine news article about ..." | R3, R5 |
| 8 | Set Technology/Business/Health/Entertainment/Sports | Категорията се знае само от клона | `category` константа, `timestamp` = `$now.toISO()` | R4 |
| 9 | Send To Reject Article (Execute Workflow) | Изолира Stop and Error за всяка спам статия | Run once for each item, Wait For Sub-Workflow = off | R5 |
| 10 | Merge Classified | Събира 5-те клона | Append, 5 inputs | R6 |
| 11 | Select Title And Text (Set) + Aggregate Articles | Статистика: масив `{title, text}` | Include Other Fields = off; All Item Data -> `articles` | R6 |
| 12 | Save To Data Table | Един ред на изпълнение със статистиката, за polling | таблица `smart_content_statistics`: `batchId`, `generatedAt`, `articleCount`, `statistic` (JSON string на масива) | (добавка) |

Reject Article: Execute Workflow Trigger -> Stop and Error със заглавие и текст (до 500 символа) в съобщението. Error Handler: Error Trigger -> Set -> Telegram (R7, R8).

## Допускания и credentials
- Credentials: OpenRouter, Telegram (нужни са само имената; id-тата са от експортите на Здравко).
- Data Table `smart_content_statistics` се създава ръчно с колони: batchId (String), generatedAt (String), articleCount (Number), statistic (String). Бърз старт: импорт на `test-data/smart_content_statistics_import.csv` (един примерен ред `sample`, за да се изведат типовете; след импорта редът се изтрива). Масивът се пази като JSON string, защото колоните са скаларни; четящият го парсира с `JSON.parse`. Ако няма валидни статии, ред не се записва.
- Workflow-ът трябва да е активен (production webhook). Self-hosted: URL = `<n8n base URL>/webhook/smart-content-categorizer`.
- В Send To Reject Article се избира workflow-ът Reject Article; Error workflow се задава в Settings на Reject Article (и по желание на основния).
- Telegram chatId е същият като в домашно 03/06.

## Тестов план
Виж `test-data/expected-results.md`.

## Покритие
R1 -> 1-5, R2 -> 6, R3 -> 7, R4 -> 8, R5 -> 7 (Other) + 9 + Reject Article, R6 -> 10, 11 (+ 12 за записа), R7 -> Error Trigger + Stop and Error, R8 -> Telegram.

## Скриншоти (v3, предоставени от Здравко)
- `screenshots/execution-01.png` - Data Table `smart_content_statistics`: по един ред на изпълнение (`articleCount` 6, `statistic` JSON).
- `screenshots/execution-02.png` - успешно production изпълнение на основния workflow (Executions, `mixed`): 8 статии на входа, 6 класифицирани, 2 към Send To Reject Article.
- `screenshots/execution-03.png` - успешно production изпълнение на основния workflow с 2 статии на входа; клонът към Send To Reject Article е изпълнен.
