# Changelog - 18-personal-rag

## 2026-10-23 - Ingest v3
- Промяна: добавени `Split Segments`, `Loop Over Segments`, `Wait Rate Limit` (65 s); chunks 2000/200; Default Data Loader чете текущия сегмент (metadata `source`, `segment`); `embeddingBatchSize` 10; v2 е архивиран в `_versions/`.
- Причина: изпълнения 2787 и 2790 - след 100 вграждания Gemini връща празен вектор (лимит 100 заявки/мин, 1 000/ден).
- Засегнати нодове: Insert Chunks, Default Data Loader, Recursive Text Splitter, нови Split Segments, Loop Over Segments, Wait Rate Limit.

## 2026-10-23 - Ingest v2
- Промяна: txt вместо pdf, проверка за празен текст, `pdf_to_text.py` в `test-data/`.
- Причина: изпълнение 2762 - празен текст от PDF парсера (652 страници, 0 реда в таблицата).
- Засегнати нодове: Upload Manual, Extract Text, Has Text, Stop - Empty Text.

## 2026-10-23 - v1
- Промяна: нови workflow-и Ingest (`I8vF7IT8l61GJjUA`) и Ask (`LsO3QY8fZB9SqadC`) през n8n MCP; миграция `create_manual_chunks_vector_store` (vector, `manual_chunks`, `match_manual_chunks`) в Supabase проекта `weekly-shopping-assistant`; санитизирани експорти в `n8n-workflows/`.
- Причина: ново домашно (W04 HW05).
- Засегнати нодове: всички (ново).
- Смоук тест T0 на Ask: execution 2750, success (празна таблица).
