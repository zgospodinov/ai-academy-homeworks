# Тестови сценарии - 13-expense-receipt-assistant

Подготовка: Data Table `expense_policy` (Import CSV от `../attachments/expense_policy.csv`) и празна `expenses` (колони от `expenses-header.csv`; `total`, `totalEur`, `approvedAmount` са числа). В Config: `managerEmail`, `formUrl`. Форма: production URL на Expense Form. Ред: подавай 1-6 последователно, за да се тества и дубликатът.

| № | Файл (в `../attachments/receipts/`) | Служител | Очаквано |
|---|-------------------------------------|----------|----------|
| 1 | `receipt_01_cafe.jpg` | тест | Food, 18.40 EUR <= 40 -> approved автоматично; имейл със сума 18.40; ред в `expenses` (`decidedBy = policy`) |
| 2 | `receipt_04_cafe_again.jpg` (след 1) | тест | същият отпечатък (бон 004812) -> имейл "already submitted"; няма нов ред |
| 3 | `receipt_03_office_bgn.jpg` | тест | 97.80 BGN -> около 50.00 EUR, Office <= 100 -> approved; `currency = BGN`, `totalEur` около 50 |
| 4 | `receipt_02_hotel.jpg` | тест | Travel, 386 EUR > 150 -> имейл до мениджъра; ред `pending` докато чака; approve със сума и коментар -> approved, имейл със сумата. Повторно (друг служител или имейл) със същата бележка, докато чака -> дубликат |
| 4b | `receipt_02_hotel.jpg` | тест | при reject от мениджъра -> `rejected`, `approvedAmount = 0`, коментарът е в имейла (изчисти реда преди повторение) |
| 5 | `receipt_05_bowling.jpg` | тест | Entertainment, `allowed = false` -> rejected без мениджър |
| 6 | `image_06_not_a_receipt.jpg` | тест | `isReceipt = false` -> имейл за нова снимка; няма ред |
| 7 | `receipt_07_hotel_pirin.jpg` | тест | Travel, 475.50 EUR > 150 -> имейл до мениджъра; различна от бележка 2 (друг хотел, бон 2026-0342) -> НЕ е дубликат; втори независим тест на Send and Wait (напр. reject с коментар) |

Гранични случаи: (7) нечетима/повредена снимка -> error output -> имейл за нова снимка (причина "could not be read"); (8) валута, различна от EUR и BGN (напр. USD) -> към мениджъра.

Бонуси: B1 пусни Manual Trigger след сценарии 1-5 (редовете трябва да са решени през последната седмица); B2 в чата: "How much did I spend on travel?" -> пита за имейл, после сумата; B3 нарочно счупи credential в Read Receipt, за да видиш Error Alert (Error Workflow е избран в Settings).

Какво да се провери при първия run (непотвърдено): име на binary полето от формата; дали Set нодовете пазят binary; Image (Binary) съобщението в Basic LLM Chain; number поле в Custom Form; типове на колоните след CSV импорт.
