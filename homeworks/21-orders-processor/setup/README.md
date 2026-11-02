# Orders Processor - setup на нова n8n инстанция

Шаблони за бързо създаване на ресурсите, от които зависи домашно 21. Данните са измислени.

## Data Tables (n8n: Data tables -> Create -> Import CSV)
| Файл | Таблица | Бележка |
|------|---------|---------|
| `data-tables/orders_eval_dataset.csv` | `orders_eval_dataset` | 16 eval случая; колоните `actual_*` са празни, попълват се при пускане |
| `data-tables/orders_eval_images.csv` | `orders_eval_images` | 2 умалени тестови снимки (base64), оригиналите са в `../test-data/` |
| `data-tables/orders_ledger.csv` | `orders_ledger` | само заглавия; защита от дубликати на имейла |

След импорт избери таблиците наново във възлите с Data table (Evaluation Trigger, Get Eval Images, Find/Claim/Mark Order, Eval Runner), защото ID-тата са различни.

## Google Sheet (един документ, всеки CSV е отделен таб)
`sheets/suppliers.csv`, `purchase_orders.csv`, `jailbreak_log.csv`, `error_log.csv`, `eval_results.csv`. Таб `suppliers` е с примерни доставчици. Сложи ID на новия документ във всички Sheets нодове.

## Supabase
`supabase-setup.sql` - разширение `vector`, таблици `supplier_chunks` (embedding 3072) и `supplier_sync_state`, функция `match_supplier_chunks`.

## Ръчни стъпки
Пълният списък е в Sticky Note "Prerequisites" в основния workflow.
