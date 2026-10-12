# Очаквани резултати - 08-customer-feedback-sentiment

Вход: `feedback-samples.json` (8 отзива + 1 празен).

| Проверка | Очаквано |
|----------|----------|
| Customer Feedback Samples | 8 items (празният fb-009 е махнат) |
| Sentiment Analysis | 3 Positive, 2 Neutral, 3 Negative (моделът може да се отклони при гранични отзиви като fb-004) |
| Negative Feedback Output | само fb-003, fb-004, fb-006, с `analyzedAt`, `sentiment`, `strength`, `confidence` |
| Flag Urgent Cases | fb-003 и fb-006 -> `isUrgent = true`; fb-004 -> `false` (при прагове 0.7 / 0.7) |
| Send Email | ОДИН имейл, темата започва с `[URGENT]`, спешните са най-отгоре |

Гранични случаи:
- Без негативни отзиви: Filter Negative не връща items, имейл не тръгва.
- Скалата на strength/confidence и точните имена на полетата (`sentimentAnalysis.category/strength/confidence`) се потвърждават по реалния изход на първия тест; при нужда се нагласят Enrich Feedback и праговете.

## v3 - допълнителни проверки
| Проверка | Очаквано |
|----------|----------|
| Нормално пускане | както във v2; един имейл с таблицата (Aggregate -> Build Email) |
| Без позитивни/неутрални отзиви | потокът пак минава и праща един имейл |
| Без негативни | имейл не тръгва |
| Счупен OpenRouter credential | след опитите за повторение - един имейл `[ERROR] Sentiment analysis failed for N feedback(s)` |
| Прагове в Config (напр. 0.9) | `isUrgent` се променя без промяна на други нодове |
