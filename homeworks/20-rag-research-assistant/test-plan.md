# 20-rag-research-assistant - Тестов план

- Статус: `executed` (T1-T9 минали с Agent v3c; I1 проверен със SQL; I2, I3 не са пускани)
- Версия на workflow: Ingest v1, Agent v1 (T1-T9 пуснати), Agent v2 приложен, чака повторни тестове
- Режим: ръчен (Здравко, Chat панел) / MCP manual
- Обновено: 2026-10-24 (резултати)

## Предпоставки
- Credentials: Google Gemini(PaLM) - Encorp AI Academy; Supabase - Weekly Shopping Assistant; Postgres Weekly Shopping Assistant; OpenRouter Encorp Academy Homeworks; **SerpApi** (Query Auth, `api_key`) - за T4-T9.
- Данни: статията се чете от Wikipedia при Ingest. Въпросите и SQL проверките са в `test-data/test-questions.md` и `test-data/verify_in_doc.sql`.
- **Преди T1-T3 и T9 (част RAG)** пусни `verify_in_doc.sql`: всеки въпрос "от документа" трябва да има подкрепящ chunk. Въпрос без chunk се сменя, не се подгонва отговорът.
- Как се вижда кой инструмент е ползван: в изпълнението (Executions) на Agent workflow-а се гледат нодовете `RAG Search` и `Web Search`; допълнително редът `Source:` в края на отговора.

## Сценарии

### Индексиране (Ingest)

| № | Вид | Вход | Очакван резултат | Покрива | Странични ефекти | Резултат | Оценка |
|---|-----|------|------------------|---------|------------------|----------|--------|
| I1 | основен | Ingest, ръчно пускане | редове в `ai_wiki_chunks` (около 70-100), `vector_dims = 3072`, `metadata.source` = URL на статията, без грешки | R1 | Wikipedia GET, запис в Supabase, Gemini embeddings | Изпълнение #3302 (success, около 2.5 мин). SQL: 61 реда, `vector_dims` 3072 (мин и макс), 2 сегмента. По-малко от очакваните 70-100 chunks (статията е по-къса от оценката) | passed |
| I2 | граничен | Ingest втори път | броят редове не се удвоява (Delete Old Chunks) | бонус | запис в Supabase, Gemini embeddings (дневен лимит 1 000) | Не е пускан | skipped |
| I3 | граничен | Wikipedia върне празен текст (напр. грешно заглавие в тестово копие) | `Stop - Empty Text`, грешка, 0 нови реда | надеждност | няма | Не е пускан | skipped |

### Агент (Agent)

Правило за всички: RAG Search се вика първи; Web Search само ако откъсите не съдържат отговора.

| № | Вид | Въпрос | Очаквани инструменти | Очакван `Source:` | Покрива | Странични ефекти | Резултат | Оценка |
|---|-----|--------|----------------------|-------------------|---------|------------------|----------|--------|
| T1 | в документа | What was the Dartmouth workshop of 1956? | само RAG Search | Wikipedia KB (RAG) | R3, R5, R6 | Gemini embedding, OpenRouter | Здравко: покрито, само RAG | passed |
| T2 | в документа | What is an AI winter? | само RAG Search | Wikipedia KB (RAG) | R3, R5, R6 | същите | Здравко: покрито, само RAG | passed |
| T3 | в документа, друг език | Какво е тестът на Тюринг? | само RAG Search (английска заявка), отговор на български | Wikipedia KB (RAG) | R3, R5, R6 | същите | Здравко: покрито. Заявката към RAG Search е изпратена на български (не е преведена на английски, както казва правило 1), и пак е намерила правилния откъс | passed (с забележка: правило 1 не е спазено, резултатът е верен) |
| T4 | извън документа, актуално | What is the weather in Sofia today? | RAG Search, после Web Search | Web (SerpApi) | R4, R5, R6 | + 1 SerpApi търсене | Здравко: покрито, RAG после Web | passed |
| T5 | извън документа, актуално | Who is the current CEO of OpenAI? | RAG Search, после Web Search | Web (SerpApi) | R4, R5, R6 | + 1 SerpApi | Здравко: покрито, RAG после Web | passed |
| T6 | извън темата | What is the capital of Australia? | RAG Search, после Web Search (не отговаря от паметта) | Web (SerpApi) | R4, R5, R6 | + 1 SerpApi | Здравко: покрито, RAG после Web | passed |
| T7 | граничен, скорошно събитие за AI | What is the newest AI model released this month? | RAG Search, после Web Search | Web (SerpApi) | R4, R5, R6 | + 1 SerpApi | Здравко: покрито, но отговорът не съвпада точно с резултата от Web Search. #3316: заявката е `newest AI model released October 2023` (годината е добавена от модела), отговорът казва "October 2023"; инструментите са в правилния ред | partial |
| T8 | граничен, частично покритие | What does the article say about generative AI, and which company released the newest image generation model this month? | RAG Search, после Web Search | Wikipedia KB (RAG) + Web (SerpApi) | R3, R4, R5, R6 | + 1 SerpApi | #3317: RAG Search (`generative AI`), после Web Search с `newest image generation model release October 2023`; Source: RAG + Web. Резултатите включваха и "ChatGPT Images 2.0" (2026), а отговорът нарича DALL-E 3 (октомври 2023) "най-новия" модел - грешен факт, предизвикан от същата остаряла година | passed по критерия за инструменти; съдържанието е грешно (виж диагноза) |
| T9 | граничен, неуспешен Web Search | Въпрос като T5 при невалиден/липсващ SerpApi ключ | RAG Search, Web Search връща грешка | без измислен отговор; агентът казва, че търсенето е неуспешно | надеждност | неуспешна заявка | #3321: RAG Search, после Web Search с `current CEO of OpenAI 2023` - 401 "Invalid API key" (credential `Query Auth - SerpApi fake`). Отговор: "The RAG Search did not provide information ... I cannot answer" + `Source: Wikipedia KB (RAG)`. Няма измислен факт, но отговорът не казва, че Web Search е неуспешен, а редът Source сочи RAG | partial |

## Критерии за успех
- Всяко задължително R (R1-R6) е покрито от поне един сценарий.
- T1-T3: в изпълнението няма изпълнен нод `Web Search`; отговорът е подкрепен от откъс (виж chunks в изхода на `RAG Search`).
- T4-T7: `RAG Search` е изпълнен преди `Web Search`; отговорът идва от резултатите на Web Search, не от паметта на модела.
- T8: и двата инструмента са ползвани, отговорът казва коя част откъде е.
- T9: няма измислен факт.
- Редът `Source:` във всеки сценарий съвпада с реално ползваните инструменти.
- Успех на целия тест: T1-T8 passed. Ако агентът в T1-T3 върне "няма информация" и отиде в мрежата, това е провал на извличането (виж HW 18, T3/T6) и се записва с диагноза (какви откъси върна RAG Search), не се маскира.


## Изпълнение v1
- Дата: 2026-10-24. Пуснал: Здравко (Chat панел и ръчно пускане на Ingest). Изпълнения: Ingest #3302; Agent #3305-#3321 (T8 = #3317, T7 = #3316, T9 = #3321; останалите номера не са сверени един по един). Данните от изпълненията са прочетени през MCP (`get_workflow_execution`).
- Инструментите са избирани правилно във всички сценарии: в T1-T3 няма изпълнен `Web Search`, в T4-T9 `RAG Search` е първи и след него идва `Web Search`.

### Диагноза (от реални данни)
1. **Остаряла година в заявките към Web Search (T7, T8, T9).** Моделът няма текуща дата и сам добавя годината от паметта си: `... October 2023`, `... 2023`. Резултатът: T7 отговаря "October 2023"; T8 избира DALL-E 3 за "най-нов", макар в резултатите да има "ChatGPT Images 2.0" от 2026. Това е причината и за разминаването в T7.
2. **Неуспешен Web Search не се споменава (T9).** При 401 инструментът връща текста "Authorization failed - please check your credentials", но агентът пише само, че RAG няма отговор и поставя `Source: Wikipedia KB (RAG)`, макар нищо да не е от RAG. Критерият "агентът казва, че търсенето е неуспешно" не е изпълнен.
3. **T3:** правило 1 ("заявка на английски") не е спазено, но Gemini embeddings са многоезични и RAG Search връща верния откъс; не е грешка в резултата.

### Предложение за v2 (одобрено и приложено 2026-10-24)
- В system prompt: ред `Today's date: {{ $now.toFormat("yyyy-MM-dd") }}` (изразът се изчислява при всяко пускане) и правило: "Do not add a year or month to the web query unless the user gave one; for 'latest/newest/current' questions prefer the most recent result by date."
- В system prompt: "If a tool returns an error, tell the user that the search failed and why; end with `Source: none`."
- Повторно изпълнение на T7, T8, T9 (T9 със счупен ключ, T7/T8 с валиден).

## Изпълнение v2
- Статус: изпълнено от Здравко (2026-10-24). T7, T8, T9 покрити; T1 без регресия; T4 регресия (диагноза и поправка в "Изпълнение v3").
- Бележка за T9 (изп. #3326): отговорът казва "couldn't find ... Source: none", но не казва изрично, че търсенето е неуспешно; заявката още носи година ("2026").
- За повторно пускане (Agent v2, валиден SerpApi ключ, освен при T9):

| № | Какво се проверява | Очаквано |
|---|--------------------|----------|
| T7 | В заявката към Web Search няма година; отговорът е по най-новия резултат (напр. Kimi K3.1 Pro от 23.10.2026, ако още е на върха) | RAG, после Web; `Source: Web (SerpApi)` |
| T8 | Заявката без остаряла година; "най-нов" модел за изображения не е DALL-E 3 от 2023 | RAG + Web; `Source: Wikipedia KB (RAG) + Web (SerpApi)` |
| T9 | Със счупен ключ (напр. временно сменен credential) | отговорът казва, че търсенето е неуспешно; `Source: none` |
| T1, T4 | Регресия: T1 пак само RAG, T4 пак RAG после Web | както в v1 |

Резултатите се вписват тук след пускане (пуска ги Здравко; през MCP T4-T8 харчат от лимита 250/месец на SerpApi).

## Изпълнение v3 (2026-10-24, автоматично през n8n MCP, валиден SerpApi ключ)
- Диагноза на T4 (изп. #3328, #3329): SerpApi върна 10 резултата, нито един за София (без `answer_box`, US-геолокация); оформянето с `dataField: organic_results` изрязваше `answer_box` с времето.
- Поправка: `json_restrictor` в Web Search + по-строг промпт (виж CHANGELOG, Agent v3). Опит между v3 и v3b: изп. #3333 - отговорът беше правилен, но 132k символа и RAG не беше извикан.

| № | Изпълнение | Въпрос | Инструменти (ред) | Резултат |
|---|-----------|--------|-------------------|----------|
| T4 | #3338 | What is the weather in Sofia today? | RAG, после Web ("Sofia weather today") | Минал: времето в София от answer_box (64°F, 67% влажност), `Source: Web (SerpApi)`; отговорът от Web Search е малък |
| T7 | #3339 | What is the newest AI model released this month? | RAG, после Web | Минал: Kimi K3.1 Pro (23.10.2026), `Source: Web (SerpApi)`; заявката още съдържа "October 2026" |
| T9 (валиден ключ) | #3340 | Who is the current CEO of OpenAI? | RAG, после Web | Минал: Sam Altman; заявката още съдържа "2026" |
| T1 | #3341 | Dartmouth workshop 1956 | само RAG | Минал: `Source: Wikipedia KB (RAG)` |
| T2-подобен (извън темата) | #3342 | Who won the Champions League final in 2025? | RAG, после Web | Минал: PSG; `Source: Web (SerpApi)` |
| T3 | #3343 | Какво е тестът на Тюринг? | само RAG (заявка на български) | Минал: отговор на български, `Source: Wikipedia KB (RAG)` |

- Остатъчни слабости: gpt-4o-mini още добавя година/месец в заявката (T7, T9) въпреки правилото; не засяга верността на отговорите.

### Допълнителни изпълнения (Agent v3b/v3c)
| № | Изпълнение | Инструменти | Резултат |
|---|-----------|-------------|----------|
| T5 | #3346 | RAG, после Web | Минал: Sam Altman, `Source: Web (SerpApi)` |
| T6 | #3347 | RAG, после Web | Минал: Canberra, `Source: Web (SerpApi)` |
| T9 (счупен ключ, v3b) | #3349 | RAG, после Web (401) | **Не мина**: "I couldn't find ... Source: none" без да каже, че търсенето е неуспешно |
| T9 (счупен ключ, v3c) | #3350 | RAG, Web (401) | Минал: "The web search failed: Authorization failed - please check your credentials. RAG Search had no answer either." `Source: none` |
| T8 | #3351 | RAG (`generative AI`), после Web | Минал: тезата от статията + Canva (22.10.2026), `Source: Wikipedia KB (RAG) + Web (SerpApi)` |
| T4 (регресия v3c) | #3352 | Web, отговор от answer_box | Минал: 64°F, `Source: Web (SerpApi)` |
| T1 (регресия v3c) | #3353 | само RAG | Минал |

- Поправка v3c: правило 5 в промпта е пренаписано (задължително изречение "The web search failed: ..."). Credential-ът на Web Search е върнат към валидния `Query Auth - SerpApi`.
- Не са пускани: I2 (повторен Ingest) и I3 (празен текст) от Ingest плана.

