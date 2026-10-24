# 20-rag-research-assistant - RAG-Powered Research Assistant

- Седмица: 4
- Домашно: задача 7
- Статус: `json-delivered`

## Условие (дословно)

RAG-Powered Research Assistant

1. Create a RAG system for a specific document (e.g., the Wikipedia page for "Artificial Intelligence").
2. Build a new AI agent workflow that is equipped with two tools:
   1. Tool 1: RAG Search: A tool that queries your custom vector store (from step 1).
   2. Tool 2: Web Search: A tool that searches the web (e.g., the Perplexity node, or SerpApi called through an HTTP Request node used as a tool).
3. Design a system prompt that instructs the agent to first try to answer a user's question using the RAG Search tool. If the RAG system doesn't have the answer, the agent should then use the Web Search tool.
4. Test the agent with questions you know are in your document and with questions you know are not, to ensure it uses the correct tool each time.

Note: SerpApi returns Google search results through an API and has a free plan allowing 250 searches a month. n8n's dedicated SerpApi tool node is deprecated (removed in n8n 3.0).

## Изисквания

| № | Изискване | Тип |
|---|-----------|-----|
| R1 | RAG система за конкретен документ (напр. Wikipedia "Artificial intelligence"): документът е разрязан, с embeddings, във vector store | задължително |
| R2 | Нов workflow с AI агент | задължително |
| R3 | Tool 1 - RAG Search: инструмент, който търси в собствения vector store от R1 | задължително |
| R4 | Tool 2 - Web Search: инструмент за търсене в мрежата (Perplexity нод или SerpApi през HTTP Request Tool; SerpApi нодът е deprecated) | задължително |
| R5 | System prompt: първо RAG Search; ако RAG няма отговор, тогава Web Search | задължително (критерий за оценяване) |
| R6 | Тест с въпроси, които със сигурност са в документа, и с въпроси, които със сигурност не са; агентът ползва правилния инструмент всеки път | задължително (критерий за оценяване) |

## Отворени въпроси

| № | Въпрос / неяснота | Засяга | Тежест | Предложено допускане | Статус | Отговор |
|---|-------------------|--------|--------|----------------------|--------|---------|
| Q1 | Кой Web Search инструмент: SerpApi през HTTP Request Tool или Perplexity? В n8n няма credential нито за SerpApi, нито за Perplexity | R4 | блокиращ | SerpApi през HTTP Request Tool (безплатен план 250 търсения/месец, достатъчно за теста) | answered | SerpApi през HTTP Request Tool (Здравко, 2026-10-24). Ключът още не е в n8n: създава се Query Auth credential |
| Q2 | Кой документ и откъде? | R1 | неблокиращ | Английската Wikipedia "Artificial intelligence", чист текст през MediaWiki API (`prop=extracts&explaintext=1`); чете се от n8n, не се качва на ръка | assumed | Прието с одобрението на плана (2026-10-24) |
| Q3 | Кой vector store и embedding модел? | R1, R3 | неблокиращ | Supabase pgvector в проекта `weekly-shopping-assistant`, нова таблица и RPC функция (отделни от тези на домашно 18), Gemini `gemini-embedding-001` (3072), като в домашно 18 | assumed | Прието с одобрението на плана (2026-10-24) |
| Q4 | Кой LLM за агента? | R2 | неблокиращ | OpenRouter `openai/gpt-4o-mini`, temperature 0 (като в домашни 15-19) | assumed | Прието с одобрението на плана (2026-10-24) |
| Q5 | Тригер | R2 | неблокиращ | Chat Trigger | assumed | Прието с одобрението на плана (2026-10-24) |
| Q6 | Един или два workflow-а? | R1, R2 | неблокиращ | Два: `Ingest` (R1) и `Agent` (R2-R5), както в домашно 18 | assumed | Прието с одобрението на плана (2026-10-24) |
| Q7 | Как агентът решава "RAG няма отговор"? Vector търсенето винаги връща топ-K откъса, дори да са нерелевантни | R5 | неблокиращ | Агентът сам преценява дали върнатите откъси отговарят на въпроса (правило в system prompt), без числов праг; отговорът завършва с ред `Source: Wikipedia KB (RAG)` или `Source: Web (SerpApi)`, за да се вижда кой инструмент е ползван | assumed | Прието с одобрението на плана (2026-10-24) |
| Q8 | Нужна ли е памет? | R2 | неблокиращ | Не (условието не я иска; всеки въпрос е самостоятелен) | assumed | Прието с одобрението на плана (2026-10-24) |
| Q9 | Как се доказва кой инструмент е ползван? | R6 | неблокиращ | Изпълнението в n8n (кои tool нодове са се изпълнили) плюс реда `Source:` в отговора; резултатите отиват в `test-plan.md` | assumed | Прието с одобрението на плана (2026-10-24) |
| Q10 | Версионен риск: `Supabase Vector Store` като инструмент на агент (режим retrieve-as-tool) в n8n 2.41.6; SerpApi нодът е deprecated | R3, R4 | неблокиращ | Режимът и параметрите се потвърждават с `get_node_types` преди изграждане; за SerpApi се ползва `httpRequestTool` 4.5 (потвърдено в домашно 07) | assumed | Прието с одобрението на плана (2026-10-24) |
