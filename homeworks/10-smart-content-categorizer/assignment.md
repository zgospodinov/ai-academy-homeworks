# 10-smart-content-categorizer - Smart Content Categorizer

- Седмица: 3 (Encorp AI Academy 2026)
- Домашно: задача 3
- Статус: `tested`

## Условие (дословно)

Task:

1. Use a Webhook trigger to receive an array of short article submissions. The webhook will be triggered from an HTTP Request node that will make manual POST requests (you can place the HTTP Request node in the same workflow)
2. Split the articles into separate items
3. Use Text Classifier to categorise articles into: Technology, Business, Health, Entertainment, Sports
4. Use the Edit node to add "category" and "timestamp" fields to each article
5. If the article cannot be categorised (e.g. it is a spam message, not an article), output it in the "Other" branch and use the Stop and Error node to cut the execution
6. Merge all classified articles into one single statistic

Bonus:

1. Set up an Error workflow that will handle the error trigger by getting the article text and
2. sending it to Slack/Telegram/Email (by choice)

## Изисквания

| № | Изискване | Тип |
|---|-----------|-----|
| R1 | Webhook trigger, получава масив от кратки статии; HTTP Request (в същия workflow) прави ръчни POST заявки | задължително |
| R2 | Разделяне на статиите на отделни items | задължително |
| R3 | Text Classifier: Technology, Business, Health, Entertainment, Sports | задължително |
| R4 | Edit нод добавя `category` и `timestamp` към всяка статия | задължително |
| R5 | Некатегоризируема статия (напр. спам) -> клон "Other" -> Stop and Error прекъсва изпълнението | задължително |
| R6 | Merge на всички класифицирани статии в една обща "статистика" (уточнение на Здравко: масив от обекти със `title` и `text`) | задължително |
| R7 | Error workflow с Error Trigger, който взима текста на статията | бонус |
| R8 | Изпращане на текста към Slack/Telegram/Email (по избор) | бонус |

## Критерии за оценяване

_(не са посочени в условието)_
