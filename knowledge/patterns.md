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
