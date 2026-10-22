# 17-system-prompt-fun - System Prompt Fun

- Седмица: 4
- Домашно: задача 4
- Статус: `tested`

## Условие (дословно)

System Prompt Fun

1. Using the system prompt template from the presentation, write a detailed prompt for an AI agent with a specific persona. The persona could be "A 1920s detective explaining AI concepts" or "A cheerful librarian identifying books from descriptions." (or some other fun persona)
2. Your prompt must include sections for:
   1. Role and Objective
   2. Instructions & Constraints
   3. Reasoning/Thinking Steps
   4. Output Format (e.g., must respond in Markdown)
3. Implement this system prompt in an n8n AI agent workflow and test it with several user prompts to see if the AI consistently adheres to the persona and rules you defined.

## Изисквания

| № | Изискване | Тип |
|---|-----------|-----|
| R1 | Детайлен system prompt за агент с конкретна персона, по шаблона от презентацията | задължително |
| R2 | Секция Role and Objective | задължително |
| R3 | Секция Instructions & Constraints | задължително |
| R4 | Секция Reasoning/Thinking Steps | задължително |
| R5 | Секция Output Format (напр. Markdown) | задължително |
| R6 | Промптът е имплементиран в n8n workflow с AI агент | задължително |
| R7 | Тест с няколко потребителски заявки и преценка дали агентът последователно спазва персоната и правилата | задължително (критерий за оценяване) |

## Отворени въпроси

| № | Въпрос / неяснота | Засяга | Тежест | Предложено допускане | Статус | Отговор |
|---|-------------------|--------|--------|----------------------|--------|---------|
| Q1 | Седмица и номер на задачата за името на workflow-а | име | блокиращ | Седмица 4, задача 4 | answered | От съобщението на Здравко |
| Q2 | Каква персона | R1 | блокиращ | - | answered | Шеговит автомонтьор |
| Q3 | Език на промпта и отговорите | R1, R5 | блокиращ | - | answered | Всичко на български |
| Q4 | Шаблонът от презентацията не е наличен; имената на секциите може да са други | R2-R5 | неблокиращ | Четирте секции от условието, дословно като заглавия; допълнителна секция "Examples" само ако шаблонът я има | assumed | Прието с одобрението на плана (2026-10-22) |
| Q5 | Тригер | R6 | неблокиращ | Chat Trigger (свободен текст, тест в чата на n8n) | assumed | Прието с одобрението на плана (2026-10-22) |
| Q6 | LLM | R6 | неблокиращ | OpenRouter Chat Model, `openai/gpt-4o-mini`, temperature 0.7 (за жив тон; по-ниска стойност прави шегите еднообразни) | assumed | Прието с одобрението на плана (2026-10-22) |
| Q7 | Какво прави персоната (тематика)? | R1 | неблокиращ | Обяснява технически теми (AI, .NET, API) чрез автосервизни аналогии | assumed | Прието с одобрението на плана (2026-10-22) |
| Q8 | Памет и инструменти | R6 | неблокиращ | Без памет и без инструменти (условието не ги иска; всяка заявка е самостоятелна) | assumed | Прието с одобрението на плана (2026-10-22) |
| Q9 | Как се доказва "последователност" | R7 | неблокиращ | Тестови набор от 8 заявки (типични, извън темата, опит за излизане от роля, опит за разкриване на промпта, английски вход, празна/кратка заявка), оценка по чеклист | assumed | Прието с одобрението на плана (2026-10-22) |
