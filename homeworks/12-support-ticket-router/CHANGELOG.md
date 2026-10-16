# Changelog - 12-support-ticket-router

## 2026-10-16 - 12-support-ticket-router v2 (screenshots)
- Промяна: добавени 4 снимки от теста в `screenshots/` (имейл, форма за ревю, Google Tasks), описани в `solution-plan.md`. Изрязани, за да не съдържат лични данни.
- Причина: искане на Здравко - потвърждение от теста.
- Засегнати нодове: няма.

## 2026-10-16 - 12-support-ticket-router v2 (tested)
- Промяна: няма промяна във файла; Здравко разиграл всички тестови сценарии - workflow-ът работи правилно, без проблеми. Статус -> tested.
- Причина: потвърждение от теста в неговия n8n.
- Засегнати нодове: няма.

## 2026-10-16 - 12-support-ticket-router v2
- Промяна: един workflow вместо два; ревюто е Gmail Send and Wait (Custom Form), без Data Table, без втори workflow. Добавена Sticky Note "Design considerations, alternatives and recommendations"; v1 е архивиран в `_versions`, файловете за Data Table са в `test-data/archive-v1/`.
- Причина: решение на Здравко след негово проучване - малък обем на тикетите, по-прост дизайн; чакащите изпълнения не държат worker.
- Засегнати нодове: премахнати Save Ticket As Pending, Load Ticket, Mark * и Form completion нодовете; нови Compose Review Message, Request Sentiment Review, Read Review Decision. Не е тестван.

## 2026-10-15 - 12-support-ticket-router v1
- Промяна: два workflow-а (Intake и Review) с Data Table `support_tickets` като състояние, Gmail за ревюто (форма с линк), таб `Audit Log` за историята, Sticky Notes с групи и описание на промените.
- Причина: ново домашно (седмица 3, задача 5); уточнения на Здравко при одобрението на плана.
- Засегнати нодове: всички (нов).
