# Тестови въпроси - 20-rag-research-assistant

Измислени/публични въпроси, без лични данни. Очакванията са към `test-plan.md`.

| № | Въпрос (точно както се пише в чата) | Група | Очаквани инструменти |
|---|-------------------------------------|-------|----------------------|
| T1 | What was the Dartmouth workshop of 1956? | в документа | RAG |
| T2 | What is an AI winter? | в документа | RAG |
| T3 | Какво е тестът на Тюринг? | в документа (български) | RAG |
| T4 | What is the weather in Sofia today? | извън документа | RAG, после Web |
| T5 | Who is the current CEO of OpenAI? | извън документа | RAG, после Web |
| T6 | What is the capital of Australia? | извън темата | RAG, после Web |
| T7 | What is the newest AI model released this month? | скорошно събитие | RAG, после Web |
| T8 | What does the article say about generative AI, and which company released the newest image generation model this month? | частично покритие | RAG + Web |
| T9 | Who is the current CEO of OpenAI? (със счупен SerpApi ключ) | грешка на Web Search | RAG, Web (грешка) |

Бележка: "this month" в T7/T8 е умишлено: статията е снимка от момента на индексиране и не знае за скорошни събития.
