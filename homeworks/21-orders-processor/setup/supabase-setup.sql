-- Orders Processor: Supabase setup (run once in the SQL editor)
-- Embeddings: Google Gemini, 3072 dimensions (no ANN index above 2000 dims)
create extension if not exists vector with schema extensions;

create table if not exists public.supplier_chunks (
  id bigserial primary key,
  content text,
  metadata jsonb,
  embedding extensions.vector(3072)
);

create table if not exists public.supplier_sync_state (
  id integer primary key,
  content_hash text,
  updated_at timestamptz default now()
);

alter table public.supplier_chunks enable row level security;
alter table public.supplier_sync_state enable row level security;

create or replace function public.match_supplier_chunks(
  query_embedding extensions.vector,
  match_count integer default null,
  filter jsonb default '{}'::jsonb
)
returns table(id bigint, content text, metadata jsonb, similarity double precision)
language plpgsql
set search_path to 'extensions', 'public'
as $$
begin
  return query
  select sc.id, sc.content, sc.metadata, 1 - (sc.embedding <=> query_embedding) as similarity
  from public.supplier_chunks sc
  where sc.metadata @> filter
  order by sc.embedding <=> query_embedding
  limit match_count;
end;
$$;
