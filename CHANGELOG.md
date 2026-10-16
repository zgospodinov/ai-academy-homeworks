# Changelog

## 2026-10-16 - 12-support-ticket-router (само документация)
- Промяна: добавени 4 снимки от теста в `homeworks/12-support-ticket-router/screenshots/` (имейл за ревю, форма, Google Tasks) - оригинални, непроменени.
- Причина: искане на Здравко - потвърждение от теста.
- Засегнати нодове: няма.

## 2026-10-16 - 12-support-ticket-router v2 (tested)
- Промяна: няма промяна във файла; потвърдено от Здравко, че всички тестови сценарии работят без проблеми (Gmail Send and Wait Custom Form, Google Sheets Tool, Google Tasks Tool). Статус -> tested.
- Причина: потвърждение от теста в неговия n8n.
- Засегнати нодове: няма.

## 2026-10-16 - 12-support-ticket-router v2
- Промяна: един workflow с Gmail Send and Wait (Custom Form) вместо два workflow-а и Data Table; добавена Sticky Note "Design considerations, alternatives and recommendations"; v1 е в `n8n-workflows/_versions/12-support-ticket-router/`, файловете за Data Table - в `test-data/archive-v1/`.
- Причина: Здравко реши по-прост дизайн при малък обем на тикетите, след собствено проучване за влиянието на Wait/HITL възлите.
- Засегнати нодове: премахнати Data Table, Load/Mark и Form completion нодове; нови Compose Review Message, Request Sentiment Review, Read Review Decision. Не е тестван.

## 2026-10-16 - 12-support-ticket-router (само документация)
- Промяна: добавен `homeworks/12-support-ticket-router/test-data/support_tickets_import.csv` за импорт на Data Table.
- Причина: искане на Здравко - по-лесно създаване на таблицата.
- Засегнати нодове: няма.

## 2026-10-15 - 12-support-ticket-router v1
- Промяна: нов домашен - два workflow-а (Intake и Review): Form Trigger, Sentiment Analysis, Text Classifier, Data Table като състояние на тикета, Gmail ревю през форма, AI Agent с Google Sheets Tool и Google Tasks Tool, таб `Audit Log`.
- Причина: ново домашно (седмица 3, задача 5); Здравко одобри плана с Data Table вместо Send and Wait (без изчакващи изпълнения).
- Засегнати нодове: всички (нов). Не е тестван.

## 2026-10-15 - 11-meeting-notes-summariser v2 (tested)
- Промяна: няма промяна във файла; потвърдено от Здравко, че главният поток работи (Date & Time, Attach Date). Статус -> tested.
- Причина: потвърждение от теста в неговия n8n.
- Засегнати нодове: няма.

## 2026-10-14 - 11-meeting-notes-summariser v2
- Промяна: поправено четене на изхода на Summarization Chain (обект `{text}` / `{output_text}`) в 3 нода; добавен `comparison.md` с резултата от бонуса.
- Причина: реален изход от бонус клона на Здравко.
- Засегнати нодове: Build Comparison, Label Department Summaries, Attach Date To Summary.

## 2026-10-14 - 11-meeting-notes-summariser v1
- Промяна: нов домашен - workflow с 20 нода (Summarization Chain Map Reduce в два етапа, Date & Time, бонус сравнение на методите).
- Причина: ново домашно (седмица 3, задача 4).
- Засегнати нодове: всички (нов).

## 2026-10-14 - 10-smart-content-categorizer v3 (потвърдена)
- Промяна: няма; Здравко потвърди, че всички сценарии (mixed, valid, spam_only, invalid) работят правилно. Статус -> tested.
- Причина: потвърждение от теста в неговия n8n.
- Засегнати нодове: няма.

## 2026-10-14 - 10-smart-content-categorizer v3
- Промяна: Text Classifier получава собствен System Prompt (Options -> System Prompt Template) и по-строги описания на категориите ("Genuine news article about ...").
- Причина: тест на Здравко с v2 - спамът не се засичаше (в `mixed` всичките 8 са станали статии; при повторно пускане засечен 1 от 2; в `spam_only` всички минават като статии). Стандартният промпт не обяснява кога да се избере fallback.
- Засегнати нодове: Text Classifier, Sticky Note. Останалото е непроменено спрямо v2 (v2 е в `_versions/`).

## 2026-10-14 - 10-smart-content-categorizer v2
- Промяна: в Data Table се записва един ред със статистиката (`batchId`, `generatedAt`, `articleCount`, `statistic` като JSON низ), а не ред за всяка статия. Редът на нодовете: Merge -> Select Title And Text -> Aggregate Articles -> Save To Data Table. Таблицата е `smart_content_statistics`.
- Причина: корекция от Здравко веднага след v1 (v1 не е тествана).
- Засегнати нодове: Save To Data Table (нови колони), Aggregate Articles и Select Title And Text (преди записа), Sticky Note. Reject Article и Error Handler са непроменени.

## 2026-10-14 - 10-smart-content-categorizer v1
- Промяна: нов домашен - основен workflow, под-workflow Reject Article и Error Handler (3 файла). Асинхронен webhook (202), Stop and Error в изолиран под-workflow, запис в Data Table.
- Причина: ново домашно (седмица 3, задача 3); промени по искане на Здравко при одобрението на плана.
- Засегнати нодове: всички (нов).

## 2026-10-13 - 09-job-application-screening v3 (потвърдена)
- Промяна: няма; Здравко потвърди успешен тест. Статус -> tested.
- Причина: потвърждение от теста в неговия n8n.
- Засегнати нодове: няма.

## 2026-10-13 - 09-job-application-screening v3
- Промяна: ръчен тригер с 5 тестови кандидата през Execute Workflow към същия workflow; нодовете от Config нататък са непроменени спрямо v2 (тестваният експорт е в _versions/).
- Причина: автоматично тестване без ръчно попълване на формата.
- Засегнати нодове: само нови нодове преди Config.

## 2026-10-13 - 09-job-application-screening v2
- Промяна: Cell Format = Let n8n format в Append to Google Sheet; v1 е в _versions/.
- Причина: телефон с водещ `+` се записваше като формула (`#ERROR!`).
- Засегнати нодове: Append to Google Sheet.

## 2026-10-13 - 09-job-application-screening v1
- Промяна: първа доставка (Form Trigger, Information Extractor, Code проверка, IF, Basic LLM Chain скоринг, Google Sheets).
- Причина: ново домашно (седмица 3, задача 2).
- Засегнати нодове: всички.

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
