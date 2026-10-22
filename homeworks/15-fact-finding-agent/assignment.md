# 15-fact-finding-agent - The Fact-Finding Agent

- Седмица: 4
- Домашно: задача 2
- Статус: `tested`

## Условие (дословно)

The Fact-Finding Agent

1. Create an n8n workflow for an AI agent.
2. Equip the agent with at least two tools: a Calculator and the Wikipedia API tool.
3. The agent's goal is to answer multi-step questions that require both calculation and information retrieval.
4. Test it with a prompt like: "According to Wikipedia, how many years did Queen Victoria reign? Multiply that number by 3."
5. Ensure the agent correctly identifies which tool to use for each part of the prompt and returns a final, accurate answer.

## Изисквания

| № | Изискване | Тип |
|---|-----------|-----|
| R1 | n8n workflow с AI агент | задължително |
| R2 | Агентът има поне два инструмента: Calculator и Wikipedia | задължително |
| R3 | Агентът отговаря на многостъпкови въпроси, които изискват и търсене, и изчисление | задължително |
| R4 | Тест с примерния въпрос за кралица Виктория (очаквано: 63 години x 3 = 189) | задължително |
| R5 | Агентът избира правилния инструмент за всяка част от въпроса и връща точен краен отговор | задължително (критерий за оценяване) |

## Отворени въпроси

| № | Въпрос / неяснота | Засяга | Тежест | Предложено допускане | Статус | Отговор |
|---|-------------------|--------|--------|----------------------|--------|---------|
| Q1 | Седмица и номер на задачата за името на workflow-а | име | блокиращ | Седмица 4, задача 2 | answered | От съобщението на Здравко |
| Q2 | Тригер не е зададен | R1 | неблокиращ | Chat Trigger (въпросите са свободен текст, тества се в чата на n8n) | assumed | Прието с одобрението на плана (2026-10-22) |
| Q3 | LLM не е зададен | R1 | неблокиращ | OpenRouter Chat Model, `openai/gpt-4o-mini`, temperature 0 (като в домашно 13) | assumed | Прието с одобрението на плана (2026-10-22) |
| Q4 | "Wikipedia API tool" - готовият Wikipedia нод или HTTP Request Tool към Wikipedia API? | R2 | неблокиращ | Готовият Wikipedia tool нод (без credentials) | assumed | Прието с одобрението на плана (2026-10-22) |
| Q5 | "Колко години" - 63 цели години или 63.6 (63 г. и 216 дни)? | R4, R5 | неблокиращ | Цели години, ако Wikipedia ги дава изрично (63); 63 x 3 = 189 | assumed | Прието с одобрението на плана (2026-10-22) |
| Q6 | Нужна ли е памет за разговора? | R1 | неблокиращ | Не (условието не я иска; всеки въпрос е самостоятелен) | assumed | Прието с одобрението на плана (2026-10-22) |
