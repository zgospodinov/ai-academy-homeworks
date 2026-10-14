# Тестове - 10-smart-content-categorizer

Предусловия: workflow-ите са запазени и активни, Reject Article е избран в Send To Reject Article, Error Handler е зададен като Error workflow, Data Table `smart_content_statistics` е създадена (batchId, generatedAt, articleCount, statistic).
Промяна на сценария: константата `SCENARIO` в Code нода `Test Articles`.

| Сценарий | Очакван HTTP отговор | Основно изпълнение | Допълнително |
|----------|----------------------|--------------------|--------------|
| `mixed` (6 валидни + 2 спам) | 202 `{"status":"accepted","received":8}` | Success; Aggregate Articles: `articles` с 6 обекта `{title, text}`; **1 ред** в Data Table (`articleCount` 6, `statistic` = JSON низ с 6 обекта) | 2 неуспешни изпълнения на Reject Article; 2 съобщения в Telegram (заглавие + текст на спама) |
| `valid` | 202, received 6 | Success, 1 ред (`articleCount` 6) | няма грешки |
| `spam_only` | 202, received 2 | **Непотвърдено:** Merge без входове вероятно не се изпълнява; очаквам Success без статистика и без нов ред в Data Table | 2 неуспешни Reject Article, 2 Telegram |
| `invalid` (`articles: []`) | 400 | Success, спира след Respond 400 | - |

Очаквана класификация (модел, може да варира): Chipmaker -> Technology; Central bank -> Business; Daily walking -> Health; Summer blockbuster -> Entertainment; Local club -> Sports; Logistics startup -> Business.

При `mixed` провери и дали спам статия не е записана едновременно като статия и като отхвърлена: Text Classifier не налага изключителност и ако моделът върне и категория, и `fallback`=true, item-ът излиза и от двата изхода (виж в Aggregate Articles и в таблицата дали има спам заглавие).

Резултати от теста на Здравко (2026-10-14, v2): sub-workflow-ите и Telegram работят; `invalid` -> 400 (празен масив и липсващ `articles`) работи; `valid` работи; `mixed` и `spam_only` - спамът не се засича (v2, стандартен промпт). v3 (собствен System Prompt на Text Classifier): Здравко потвърди, че всички сценарии работят правилно (2026-10-14).

Production изпълненията се гледат в Executions на основния workflow (не при ръчно натискане на Execute workflow).
