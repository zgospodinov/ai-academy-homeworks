# Solution plan - 08-customer-feedback-sentiment

- Статус: `tested`
- Версия: v3 (v1 и v2 са в _versions/)
- Workflow име: `Encorp | Homework | Week 03 | HW 01 | Customer Feedback Sentiment`
- Таг: `encorp-homework`

## Изисквания
R1 Manual trigger + примерни отзиви; R2 Sentiment Analysis; R3 обогатяване (timestamp + scores); R4 филтър на негативните; R5 изход само с негативните; R6 (бонус) имейл; R7 (бонус) прагове за strength/confidence.

## Схема
```
Manual Trigger -> Customer Feedback Samples -> Sentiment Analysis -+- Positive -+
                                                ^ OpenRouter Chat  |- Neutral  -+-> Merge Results -> Enrich Feedback -> Filter Negative
                                                  Model (temp 0)   +- Negative -+                                            |
                                         +-----------------------------------------------------------------------------------+
                                         v                                                   v
                              Negative Feedback Output (NoOp) [R5]       Flag Urgent Cases -> Build Email -> Send Email [R7, R6]
```

## Нодове
| № | Нод | Защо | Ключови параметри | Покрива |
|---|-----|------|-------------------|---------|
| 1 | Manual Trigger | Ръчно пускане | - | R1 |
| 2 | Customer Feedback Samples (Code) | Много items наведнъж; пази от празен текст | 8 отзива + 1 празен | R1 |
| 3 | Sentiment Analysis | Класификация, изход на категория | Text `{{ $json.feedback }}`; Include Detailed Results | R2, R3 |
| 4 | OpenRouter Chat Model | LLM за нода | temperature 0 | R2 |
| 5 | Merge Results | Събира трите изхода, за да няма многократно изпълнение надолу (и няколко имейла) | Append, 3 inputs | R3 |
| 6 | Enrich Feedback (Set) | `analyzedAt`, `sentiment`, `strength`, `confidence` | Include Other Fields | R3 |
| 7 | Filter Negative | Само негативните | `sentiment` equals `Negative` | R4 |
| 8 | Negative Feedback Output (NoOp) | Явна изходна точка | - | R5 |
| 9 | Flag Urgent Cases (Set) | `isUrgent` | strength >= 0.7 И confidence >= 0.7 | R7 |
| 10 | Build Email (Code) | Един HTML имейл, спешните първи | runOnceForAllItems | R6, R7 |
| 11 | Send Email (Gmail) | Изпраща имейла | HTML | R6 |

## Алтернативи
- Директно свързване на трите изхода към Enrich (без Merge): всичко надолу се изпълнява по веднъж на непразен клон, имейлът тръгва няколко пъти.
- Switch/IF вместо Sentiment Analysis: не отговаря на условието.

## Допускания и credentials
- Credentials: `OpenRouter account`, `Gmail account`; `sendTo` -> реален адрес.
- strength/confidence са оценки на модела; 0.7/0.7 са стартови прагове.
- Риск: имената на изходните полета и скалата на scores, както и typeVersion 1.1 на Sentiment Analysis, не са потвърдени (няма такъв нод в досегашните експорти).
- Риск: Merge с празен вход (Append, 3 inputs) - ако блокира, свързваме изходите директно с `Enrich Feedback` и слагаме Aggregate преди имейла.

## Тестов план
Виж `test-data/`.

## Покритие
R1 -> 1-2; R2 -> 3-4; R3 -> 3, 5, 6; R4 -> 7; R5 -> 8; R6 -> 10-11; R7 -> 9-10.

## Потвърждение
- 2026-10-13: Здравко потвърди, че изпълнението работи (v2). Имейлът се рендира като таблица (Send Email без изрично `emailType`).
- Нетествано: поведение на Merge Results при празен клон (напр. когато няма Positive или Neutral отзиви).

## v3 (2026-10-13) - одобрена промяна на плана
Схема: Manual Trigger -> Config -> Customer Feedback Samples -> Sentiment Analysis (+ OpenRouter Chat Model); три изхода -> Enrich Feedback -> Filter Negative -> (Negative Feedback Output | Flag Urgent Cases -> Aggregate Negative Feedback -> Build Email -> Send Email); error изход -> Build Failure Alert -> Send Failure Alert.

- Config: прагове (0.7 / 0.7) и получател на едно място.
- Retry: 3 опита / 2000 ms на Sentiment Analysis, Send Email, Send Failure Alert; Max Retries = 3 на OpenRouter Chat Model.
- On Error = Continue (using error output) на Sentiment Analysis.
- Без Merge; Aggregate преди имейла; custom System Prompt (скала 0-1).
- Рискове: Retry на Sentiment Analysis може да не се задейства (нодът поглъща грешките); формата на error изхода (поле `error`) се потвърждава по изпълнение; опцията Max Retries на OpenRouter Chat Model не е потвърдена.
- Тестове: нормално пускане; без позитивни/неутрални; без негативни (няма имейл); счупен OpenRouter credential (имейл за неуспелите); смяна на праговете в Config.

### Потвърждение v3 (2026-10-13)
Здравко изпълни и петте теста от плана успешно: нормално пускане, без позитивни/неутрални, без негативни, счупен OpenRouter credential (имейл за неуспелите отзиви), смяна на праговете в Config. Max Retries на OpenRouter Chat Model е потвърден, че се задейства (2026-10-13). Retry On Fail на самия Sentiment Analysis остава непотвърден.

## Скриншот
- `screenshots/execution-01.png`: получен имейл от изпълнението (таблица с негативните отзиви, спешните в червено). Аватарът и името на подателя са замъглени.
- Наблюдение: при праг 0.7 / 0.7 и fb-004 ("Delivery was slower than promised...", strength 0.80, confidence 0.90) е маркиран като спешен. Ако искаш само най-ядосаните, вдигни `strengthThreshold` (напр. до 0.85) в Config.
