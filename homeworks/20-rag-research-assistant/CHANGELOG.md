# Changelog - 20-rag-research-assistant

## 2026-10-24 - 20-rag-research-assistant Agent v3
- Промяна: Web Search връща и `answer_box` (SerpApi `json_restrictor`: резюме на answer_box + title/link/snippet на органичните резултати, `optimizeResponse` изключен); system prompt: първото действие винаги е RAG Search, държава към имената на места, никога година/месец в заявката, изрично съобщение при неуспешно или празно търсене.
- Причина: тест на Здравко - регресия на T4 (времето в София): `dataField: organic_results` изрязваше answer_box с времето и резултатите не споменаваха София. Между v3 и v3b: при първия вариант (`fields: answer_box,organic_results`) отговорът беше 132k символа и агентът прескочи RAG (изп. #3333).
- Допълнение v3c: правило 5 е пренаписано ("The web search failed: <грешка>"), защото при счупен ключ (T9, #3349) агентът пишеше само "I couldn't find". След промяната: #3350 минава.
- Засегнати нодове: Web Search (параметри), Research Assistant (systemMessage).
- n8n: workflow id `PIqiLBnwp8wy2jPN`, версия "v3c - explicit tool failure message" (непубликуван). Предишната версия: `n8n-workflows/_versions/20-rag-research-assistant-agent/v2.json`.

## 2026-10-24 - 20-rag-research-assistant Agent v2
- Промяна: system prompt на Research Assistant - добавена текуща дата (`{{ $now.toFormat('yyyy-MM-dd') }}`), правило да не се добавя година/месец към заявката и да се предпочита най-новият резултат, правило за грешка на инструмент, нов ред `Source: none`.
- Причина: тест на Здравко (T7, T8, T9) и данни от изпълнения #3316, #3317, #3321 - моделът добавяше остаряла година (2023) към заявките, а неуспешен Web Search не се споменаваше.
- Засегнати нодове: Research Assistant (само параметърът systemMessage).
- n8n: workflow id `PIqiLBnwp8wy2jPN`, версия "v2 - date in prompt, tool error rule" (непубликуван). Предишната версия: `n8n-workflows/_versions/20-rag-research-assistant-agent/v1.json`.

## 2026-10-24 - v1
- Промяна: първа версия; Ingest (Wikipedia -> Supabase vector store) и Agent (RAG Search + Web Search).
- Причина: ново домашно (седмица 4, задача 7).
- Засегнати нодове: Ingest - Start Indexing, Fetch Wikipedia Article, Prepare Document, Has Text, Stop - Empty Text, Delete Old Chunks, Split Segments, Loop Over Segments, Insert Chunks, Wait Rate Limit, Default Data Loader, Recursive Text Splitter, Gemini Embeddings; Agent - Chat Trigger, Research Assistant, OpenRouter Chat Model, RAG Search, Gemini Embeddings, Web Search.
- n8n: Ingest id `7GOMJy4Mb8iVwf2l`, Agent id `PIqiLBnwp8wy2jPN`, v1 (непубликувани). Supabase проект `weekly-shopping-assistant`.
- Отклонение от плана: една група `Research Agent` вместо две (правило за node groups).
