# Преизползваеми модели

## Многоизходен нод -> един поток (Sentiment Analysis)
Свържи всеки изход към отделен вход на Merge (Append, Number of Inputs = брой изходи), после Set за обогатяване и Filter. Така следващите нодове (напр. имейл) се изпълняват веднъж. Пример: домашно 08.

## Един имейл от много items
Code нод (Run Once for All Items) събира items в HTML таблица и връща `{subject, html}`; Gmail праща един имейл. Пример: домашно 08.

## Прагове и получател в Config нод
Set нод в началото със стойности (прагове, имейл); по-късно `$('Config').first().json.<поле>`. Пример: домашно 08 v3.

## Error output + имейл за неуспели items
On Error = Continue (using error output) -> Code, който събира грешките в един HTML -> Gmail. Пример: домашно 08 v3.

## Информационен екстрактор + данни от формата (потвърдено, домашно 09)
Information Extractor връща само `output`, не пренася входните полета. Следващият Code/Set чете формата с `$('Compose Resume Text').first().json`. Свободни умения -> категории се мапват в Code по ключови думи от Config, а LLM дава само субективната оценка (общият резултат се смята детерминирано). Пример: домашно 09.

## Тест на workflow с много входни примера без промяна на потока (потвърдено, домашно 09 v3)
Manual Trigger -> Code с N примера -> Execute Workflow (същият workflow, Run once for each item) -> Execute Workflow Trigger (Accept all data) -> първият нод на реалния поток. Пример: домашно 09 v3.

## Асинхронен webhook с изолиран Stop and Error (домашно 10, потвърдено)
Webhook (Respond to Webhook node) -> IF валидация -> Respond 202 / 400 -> обработка. Елементи, които трябва да "паднат" (напр. спам), се пращат към отделен под-workflow (Execute Workflow, each, без изчакване) със Stop and Error; Error Workflow го съобщава. Основният run не се прекъсва. Потвърдено от Здравко (домашно 10, v3, 2026-10-14): извикване на под-workflow, Telegram известие, 400 при невалиден вход, всички сценарии (mixed, valid, spam_only, invalid). За спам в Text Classifier вж. gotchas (собствен System Prompt).

## Един Chat Model към няколко Summarization Chain нода (домашно 11, бонус клон изпълнен)
Един `lmChatOpenRouter` с `ai_languageModel` връзки към няколко chain-а работи (потвърдено за 3-те паралелни chain-а в бонус клона). Паралелни клонове в execution order v1 вървят един след друг; Merge (Append, N входа) събира резултатите в реда на входовете.

## Human in the Loop с Gmail Send and Wait + Custom Form в един workflow (домашно 12 v2, потвърдено)
Gmail нод (`operation: sendAndWait`, `responseType: customForm`, `defineForm: fields`) праща имейл с бутон към форма (dropdown + бележка) и държи изпълнението в "Waiting" без лимит на изчакването. Следващият Set нод чете избраното от `$json.data[...]` (с резерв по стойност), а Set "Apply Review" записва крайната стойност в данните, като пази оригинала и флаг за промяна; детерминиран Sheets нод пише история (Audit Log). Данните от преди паузата се четат с `$('Node').first()`. Потвърдено от Здравко (2026-10-16): всички сценарии, включително паралелно чакащи тикета. Подходящо при малък обем; при стотици тикета дневно, напомняния или SLA - алтернативата е два workflow-а с Data Table като състояние (домашно 12 v1, архивиран в `n8n-workflows/_versions/12-support-ticket-router/`, НЕ е тестван): WF1 записва `status = pending_review` и праща линк, WF2 (Form Trigger) чете реда по `ticketId` и `status` и сменя статуса.
