-- Пусни в Supabase SQL Editor СЛЕД Ingest и ПРЕДИ T1-T3, T8.
-- Всеки ред трябва да върне count > 0; иначе въпросът не е "в документа" и се сменя.

select 'rows' as check, count(*) as n, min(vector_dims(embedding)) as dims_min, max(vector_dims(embedding)) as dims_max
from public.ai_wiki_chunks;

select 'T1 Dartmouth' as check, count(*) as n from public.ai_wiki_chunks where content ilike '%Dartmouth%';
select 'T2 AI winter' as check, count(*) as n from public.ai_wiki_chunks where content ilike '%AI winter%';
select 'T3 Turing test' as check, count(*) as n from public.ai_wiki_chunks where content ilike '%Turing test%';
select 'T8 generative AI' as check, count(*) as n from public.ai_wiki_chunks where content ilike '%generative AI%';

-- Проверка за дубликати след I2 (трябва да е същият брой като след I1):
select metadata->>'source' as source, count(*) as n from public.ai_wiki_chunks group by 1;
