# 16-long-term-memory-agent - Long-Term Memory Agent

- Седмица: 4
- Домашно: задача 3
- Статус: `tested`

## Условие (дословно)

Long-Term Memory Agent

1. Set up a free PostgreSQL database using Supabase.
2. Create a table in your database with the minimum required fields for agent memory: id, session_id, and message (jsonb format).
3. Build an n8n workflow where an AI agent saves the history of its conversation to the Supabase table after each interaction.
4. Before generating a new response, the agent must first retrieve the conversation history for the current session_id from the database.
5. Test the memory by having a short conversation. For example:
   1. User: "My favorite color is blue."
   2. User (in the next prompt): "What is my favorite color?"
   3. The agent should be able to answer correctly by recalling the previous message.

## Изисквания

| № | Изискване | Тип |
|---|-----------|-----|
| R1 | Безплатна PostgreSQL база в Supabase | задължително |
| R2 | Таблица с минимум полета: id, session_id, message (jsonb) | задължително |
| R3 | n8n workflow с AI агент, който записва историята в таблицата след всяко взаимодействие | задължително |
| R4 | Преди нов отговор агентът първо чете историята за текущия session_id | задължително |
| R5 | Тест: "My favorite color is blue." -> "What is my favorite color?" -> верен отговор от паметта | задължително |

## Отворени въпроси

| № | Въпрос / неяснота | Засяга | Тежест | Предложено допускане | Статус | Отговор |
|---|-------------------|--------|--------|----------------------|--------|---------|
| Q1 | Седмица и номер на задачата за името на workflow-а | име | блокиращ | Седмица 4, задача 3 | answered | От съобщението на Здравко |
| Q2 | Кой Supabase проект: съществуващият `weekly-shopping-assistant` (активен) или нов безплатен? | R1, R2 | блокиращ | Съществуващият (public схемата е празна) | answered | Съществуващият проект. Таблицата се изтрива, след като Здравко потвърди, че потокът работи (2026-10-22) |
| Q3 | Как се реализира паметта: готов Postgres Chat Memory нод (сам чете и пише) или изрични Postgres нодове за четене и запис? | R3, R4 | блокиращ | Postgres Chat Memory нод | answered | Postgres Chat Memory нод (2026-10-22) |
| Q4 | Тригер не е зададен | R3 | неблокиращ | Chat Trigger (session id идва от чата на n8n) | assumed | Прието с одобрението на плана (2026-10-22) |
| Q5 | LLM не е зададен | R3 | неблокиращ | OpenRouter Chat Model, `openai/gpt-4o-mini`, temperature 0 (като в домашно 15) | assumed | Прието с одобрението на плана (2026-10-22) |
| Q6 | Колко съобщения да се връщат от историята | R4 | неблокиращ | Прозорец от последните 20 взаимодействия | assumed | Прието с одобрението на плана (2026-10-22) |
| Q7 | Име на таблицата | R2 | неблокиращ | `n8n_chat_histories` (името по подразбиране на Postgres Chat Memory; колони id, session_id, message) | assumed | Прието с одобрението на плана (2026-10-22) |
| Q8 | Връзка n8n -> Supabase | R3 | неблокиращ | Postgres credential през Supabase pooler (session mode); при съществуващ проект се ползва готовият credential | assumed | Прието с одобрението на плана (2026-10-22) |
