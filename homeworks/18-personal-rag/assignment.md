# 18-personal-rag - Personal RAG

- Седмица: 4
- Домашно: задача 5
- Статус: `plan-approved`

## Условие (дословно)

Personal RAG

1. Find a text document to use as your knowledge source (e.g., a company's FAQ page, a chapter from a public domain book, a detailed recipe or other document of interest).
2. In Supabase, enable the vector extension and create a table for your vector store, ensuring the embedding column has the correct dimensions for the embedding model you'll use (e.g., 3072 for Gemini gemini-embedding-2).
3. Build an n8n workflow that reads your text document, splits it into smaller chunks, generates embeddings for each chunk, and uploads them to your Supabase table.
4. Create a second n8n workflow that:
   1. Takes a user's question.
   2. Generates an embedding for the question.
   3. Queries the PGVector Store/Supabase vector store to find the most relevant text chunks (retrieval).
   4. Passes the original question and the retrieved chunks to an LLM, instructing it to answer the question based only on the provided text (augmentation & generation).

## Изисквания

| № | Изискване | Тип |
|---|-----------|-----|
| R1 | Текстов документ като източник на знание | задължително |
| R2 | Supabase: включено `vector` разширение | задължително |
| R3 | Таблица за vector store с embedding колона с размер, съвпадащ с embedding модела (напр. 3072) | задължително |
| R4 | Workflow 1 (индексиране): чете документа, реже на chunks, прави embeddings, качва в Supabase | задължително |
| R5 | Workflow 2 (въпроси): приема въпрос | задължително |
| R6 | Workflow 2: embedding на въпроса | задължително |
| R7 | Workflow 2: търсене в Supabase vector store за най-близките chunks (retrieval) | задължително |
| R8 | Workflow 2: въпрос + chunks към LLM с инструкция да отговаря само от дадения текст (augmentation & generation) | задължително |

## Отворени въпроси

| № | Въпрос / неяснота | Засяга | Тежест | Предложено допускане | Статус | Отговор |
|---|-------------------|--------|--------|----------------------|--------|---------|
| Q1 | Кой документ е източник на знание и откъде се чете? | R1, R4 | блокиращ | Публичен текст с URL | answered | Собствен PDF на Здравко: ръководство за експлоатация и поддръжка на Toyota Avensis; качва се през Form Trigger; чете се с Extract From File (2026-10-23) |
| Q2 | Кой Supabase проект? | R2, R3 | неблокиращ | Съществуващият `weekly-shopping-assistant` (public схемата е празна, `vector` 0.8.2 е наличен, не е инсталиран) | assumed | Прието с одобрението на плана (2026-10-23) |
| Q3 | Кой embedding модел и размер? Условието дава пример `gemini-embedding-2` (3072) | R3, R6 | неблокиращ | Embeddings Google Gemini с наличния credential; размерът се взема от реален тест на модела, таблицата се прави с него | assumed | Прието с одобрението на плана (2026-10-23) |
| Q4 | Кой LLM за отговора? | R8 | неблокиращ | OpenRouter `openai/gpt-4o-mini`, temperature 0 (като в домашни 15-17) | assumed | Прието с одобрението на плана (2026-10-23) |
| Q5 | Тригер на workflow 2 | R5 | неблокиращ | Chat Trigger | assumed | Прието с одобрението на плана (2026-10-23) |
| Q6 | Индекс върху embedding колоната | R3 | неблокиращ | pgvector ограничава HNSW/IVFFlat индекс до 2000 измерения за `vector`, а 3072 е над лимита; за малък документ индекс не е нужен (точно търсене) | assumed | Прието с одобрението на плана (2026-10-23) |
| Q7 | Един или два workflow-а (условието казва "втори") | R4, R5 | неблокиращ | Два отделни workflow-а: `Ingest` и `Ask` | assumed | Прието с одобрението на плана (2026-10-23) |
| Q8 | На какъв език е ръководството и на какъв език са въпросите? | R8 | неблокиращ | Отговорът е на езика на въпроса, фактите са само от откъсите; езикът на PDF-а се проверява при тестовете | assumed | Прието с одобрението на плана (2026-10-23) |
| Q9 | Колко е голям PDF-ът (страници, MB)? Има лимит на размера на качване във формата и лимити на Gemini embeddings при много chunks | R4 | неблокиращ | Първо тест с ограничен брой страници (`maxPages`), после целият файл | assumed | Прието с одобрението на плана (2026-10-23) |
