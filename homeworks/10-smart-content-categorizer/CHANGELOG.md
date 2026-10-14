# Changelog - 10-smart-content-categorizer

## 2026-10-14 - 10-smart-content-categorizer v3 (потвърдена)
- Промяна: няма; всички сценарии работят правилно според Здравко. Статус -> tested.
- Причина: потвърждение от теста в неговия n8n.
- Засегнати нодове: няма.

## 2026-10-14 - 10-smart-content-categorizer v3
- Промяна: собствен System Prompt Template и по-строги описания на категориите в Text Classifier.
- Причина: обратна връзка от теста на v2 - спам статиите не се насочваха към Other. Тестът потвърди още: двата sub-workflow-а се извикват и Telegram известието идва; невалиден вход -> 400; само валидни статии -> работи.
- Засегнати нодове: Text Classifier, Sticky Note.

## 2026-10-14 - 10-smart-content-categorizer v2
- Промяна: Data Table получава един ред със статистиката (JSON низ) вместо ред на статия; таблица `smart_content_statistics`; Aggregate е преди записа.
- Причина: корекция от Здравко; v1 не е тествана (запазена в `_versions/`).
- Засегнати нодове: Save To Data Table, Aggregate Articles, Select Title And Text, Sticky Note.

## 2026-10-14 - 10-smart-content-categorizer v1
- Промяна: първа доставка (3 JSON файла).
- Причина: ново домашно; одобрен план с добавки (202 + асинхронна обработка, Stop and Error в под-workflow, Data Table).
- Засегнати нодове: всички.
