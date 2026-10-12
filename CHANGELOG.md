# Changelog

## 2026-10-13 - 08-customer-feedback-sentiment v3
- Промяна: Config с прагове и получател, Retry, error клон с имейл за неуспели отзиви, без Merge + Aggregate преди имейла, custom System Prompt (виж homeworks/08-customer-feedback-sentiment/CHANGELOG.md); v2 е в _versions/.
- Причина: подобрения, одобрени от Здравко.
- Засегнати нодове: виж changelog на домашното.

## 2026-10-13 - 08-customer-feedback-sentiment v2
- Промяна: качен експорт с ръчните корекции на Здравко (виж homeworks/08-customer-feedback-sentiment/CHANGELOG.md); v1 е в n8n-workflows/_versions/08-customer-feedback-sentiment/v1.json.
- Причина: корекции след импорт.
- Засегнати нодове: OpenRouter Chat Model, Merge Results, Filter Negative, Send Email.

## 2026-10-13 - 08-customer-feedback-sentiment v1
- Промяна: ново домашно (седмица 3, задача 1) - анализ на настроенията на клиентска обратна връзка с филтър на негативните и имейл със спешни случаи.
- Причина: ново домашно.
- Засегнати нодове: всички (нов workflow).

## 2026-10-12 - конвенция за име на workflow-ите
- Промяна: полето `name` на домашни 01-07 е във формат `Encorp | Homework | Week WW | HW MM | Short Description`; тагът `encorp-homework` е проверен. Валидаторът проверява името и тага.
- Причина: лесно разпознаване и филтриране в n8n.
- Бележка: workflow-ите, вече създадени в n8n, се преименуват ръчно там.

## 2026-10-06 - замъглени скриншоти
- Промяна: замъглени имейл адрес и аватар (домашни 02, 04, 06) и чатове на трети лица в Telegram (домашни 03, 06).
- Причина: репото е публично.
- Бележка: git историята преди този commit съдържа оригиналните снимки и неочистените JSON.

## 2026-10-06 - статус на седмица 1
- Промяна: домашни 01-07 са със статус `submitted` (тествани лично от Здравко и предадени; все още без оценка).
- Причина: потвърждение от Здравко.

## 2026-10-06 - миграция към новата структура
- Промяна: домашни 01-07 от `week-01/` преместени в `n8n-workflows/NN-slug.json` и `homeworks/NN-slug/` (с `git mv`, историята е запазена); добавени README, CHANGELOG, DECISIONS, `knowledge/node-versions.md`, `tools/validate_workflow.py`.
- Причина: единна структура, описана в skill-а `n8n-academy-homeworks`.
- Санитизиране: заменени имейли с `you@example.com` и махнати лични имена от имената на credentials (домашни 02, 04, 06, 07). Credential `id` и `instanceId` са оставени (не са тайни).
- Бележка: git историята преди миграцията съдържа неочистените версии.
