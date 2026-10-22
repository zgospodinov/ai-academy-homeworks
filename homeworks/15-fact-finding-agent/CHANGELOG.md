# Changelog - 15-fact-finding-agent

## 2026-10-22 - v2 (tested)
- Промяна: Здравко промени системния промпт в n8n - махнато е изискването за формат на крайния отговор; сега е само `Final answer: short and in the language of the question`. Позициите на нодовете са изместени с по няколко пункта от редактора.
- Причина: ръчна корекция на Здравко (мотивът не е уточнен).
- Засегнати нодове: Fact-Finding Agent (`options.systemMessage`).
- Тест: T1-T5 покрити по думите на Здравко. Статус `tested`.
- n8n: workflow id RIuJ4dtYVrCtAjA4, автозаписана версия `1680379a-62ca-44ab-a926-d9357ee2874d`; v1 е в `n8n-workflows/_versions/15-fact-finding-agent/v1.json`.

## 2026-10-22 - v1
- Промяна: нов workflow `Encorp | Homework | Week 04 | HW 02 | Fact Finding Agent` в n8n през MCP (id `RIuJ4dtYVrCtAjA4`): Chat Trigger, Fact-Finding Agent, OpenRouter Chat Model, Calculator, Wikipedia + общ Sticky Note.
- Причина: ново домашно (Седмица 4, задача 2).
- Статус: `json-delivered`, чака тест от Здравко (сценарии в `test-data/test-scenarios.md`).
