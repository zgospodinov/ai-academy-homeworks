# Changelog - 14-token-counter

## 2026-10-22 - v1
- Промяна: първо създаване в n8n през MCP (id `ZKIAUoQPdr5bCpv6`), 9 нода + 5 Sticky Notes, 4 node groups.
- Причина: ново домашно (Седмица 4, задача 1).

## 2026-10-22 - v1.2
- Промяна: Google Sheet и Gemini credential свързани; от OpenAI нода е махнат излишният параметър `images` (само текстов вход).
- Причина: забележка на Здравко - обработват се само текстови данни.
- Засегнати нодове: Message OpenAI Model, Message Gemini Model, Save to Google Sheet.

## 2026-10-22 - v1.4
- Промяна: Gemini моделите са сменени от `gemini-2.5-flash-lite`/`gemini-2.5-flash` на `gemini-3.1-flash-lite` и `gemini-3.6-flash`; обновена ценова таблица.
- Причина: 404 "no longer available to new users" за gemini-2.5-flash-lite (execution 2130).
- Засегнати нодове: Token Counter Form, Calculate Cost.

## 2026-10-22 - v1 tested
- Промяна: потокът е изцяло тестван от Здравко (OpenAI и Gemini клонове, запис в Google Sheet); експортът е добавен като `n8n-workflows/14-token-counter.json` (санитизиран).
- Статус: `tested`.
