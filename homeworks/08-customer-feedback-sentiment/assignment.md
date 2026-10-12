# 08-customer-feedback-sentiment - Анализ на настроенията в обратна връзка от клиенти

- Седмица: 3 (Encorp AI Academy 2026)
- Домашно: задача 1
- Статус: `tested`

## Условие (дословно)

Build a workflow that:

1. Uses a Manual trigger with sample customer feedback texts. Customer feedback can come from anywhere - Google Sheets, Edit Node, Code Node, etc.
2. Applies Sentiment Analysis to categorize feedback as positive, negative or neutral.
3. Enriches the feedback with timestamp and sentiment scores
4. Filters the negative feedback
5. Outputs only the negative feedback data

Bonus:

1. Send email with the list of negative feedback comments and data
2. Add strength and confidence thresholds to identify the urgent cases (very angry and unhappy customers)

## Изисквания

| № | Изискване | Тип |
|---|-----------|-----|
| R1 | Manual trigger + примерни текстове на обратна връзка (източникът е свободен) | задължително |
| R2 | Sentiment Analysis: positive / negative / neutral | задължително |
| R3 | Обогатяване с timestamp и sentiment scores | задължително |
| R4 | Филтриране на негативната обратна връзка | задължително |
| R5 | Изход само с негативните данни | задължително |
| R6 | Имейл със списък на негативните коментари и данни | бонус |
| R7 | Прагове за strength и confidence за спешни случаи | бонус |

## Критерии за оценяване

_(не са посочени в условието)_
