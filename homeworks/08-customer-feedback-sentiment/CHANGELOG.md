# Changelog - 08-customer-feedback-sentiment

## 2026-10-13 - 08-customer-feedback-sentiment v3 (потвърдена)
- Промяна: няма; Здравко потвърди успешни тестове. Статус -> tested.
- Причина: потвърждение от теста в неговия n8n.
- Засегнати нодове: няма.

## 2026-10-13 - 08-customer-feedback-sentiment v3
- Промяна: (1) нов нод Config с `strengthThreshold`, `confidenceThreshold`, `recipientEmail`; Flag Urgent Cases и Send Email ги четат оттам; (2) Retry (3 опита, 2000 ms) на Sentiment Analysis, Send Email, Send Failure Alert и Max Retries = 3 на OpenRouter Chat Model; (3) Sentiment Analysis с On Error = Continue (using error output), нови Build Failure Alert и Send Failure Alert; (4) махнат Merge Results - трите изхода отиват директно към Enrich Feedback, нов Aggregate Negative Feedback преди Build Email; (5) custom System Prompt Template.
- Причина: подобрения на надеждността и поддръжката, одобрени от Здравко (план v3).
- Засегнати нодове: Config, Sentiment Analysis, OpenRouter Chat Model, Merge Results (махнат), Enrich Feedback, Flag Urgent Cases, Aggregate Negative Feedback, Build Email, Send Email, Build Failure Alert, Send Failure Alert, Sticky Note.

## 2026-10-13 - 08-customer-feedback-sentiment v2 (потвърдена)
- Промяна: няма; Здравко потвърди успешно изпълнение. Статус -> tested.
- Причина: потвърждение от тест в неговия n8n.
- Засегнати нодове: няма.

## 2026-10-13 - 08-customer-feedback-sentiment v2
- Промяна: експорт от n8n на Здравко след импорт и ръчни корекции. Нодовете и връзките са същите; променени са credentials (негови OpenRouter и Gmail), Filter Negative (caseSensitive=true, typeValidation=strict), Merge Results (махнат празният `options`), Send Email (махнат `emailType: html`, използва се стойността по подразбиране на нода). Файлът е санитизиран (имейлът в `sendTo` -> placeholder, име на Gmail credential обобщено).
- Причина: корекции на Здравко след импорт в неговия n8n.
- Засегнати нодове: OpenRouter Chat Model, Merge Results, Filter Negative, Send Email.

## 2026-10-13 - 08-customer-feedback-sentiment v1
- Промяна: първа версия на workflow-а (Manual Trigger -> Sentiment Analysis -> Enrich -> Filter Negative -> имейл с прагове за спешни).
- Причина: ново домашно (седмица 3, задача 1).
- Засегнати нодове: всички (нов workflow).
