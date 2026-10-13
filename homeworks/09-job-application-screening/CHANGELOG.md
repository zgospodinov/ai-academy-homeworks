# Changelog - 09-job-application-screening

## 2026-10-13 - 09-job-application-screening v3 (потвърдена)
- Промяна: няма; Здравко потвърди успешен тест с петте тестови кандидата през Manual Trigger. Статус -> tested.
- Причина: потвърждение от теста в неговия n8n.
- Засегнати нодове: няма.

## 2026-10-13 - 09-job-application-screening v3
- Промяна: нодовете от Config нататък са идентични с v2. Добавени са само: Manual Trigger -> Test Candidates (5 фиктивни кандидата) -> Run Candidate Through Flow (Execute Workflow към същия workflow, режим "Run once for each item") и When Executed by Another Workflow -> Config.
- Причина: автоматично тестване без ръчно попълване на формата, без да се пипа тестваната част. Всеки кандидат минава като отделно под-изпълнение с един item, така че `.first()` в Evaluate Candidate и Prepare Sheet Row остава коректен.
- Sticky Note Test Path съдържа и очакваните резултати на петте тестови кандидата.
- Засегнати нодове: само нови (Manual Trigger, Test Candidates, Run Candidate Through Flow, When Executed by Another Workflow, Sticky Note Test Path); нова връзка към Config.

## 2026-10-13 - 09-job-application-screening v2 (потвърдена)
- Промяна: експортът на Здравко (с работеща Google Sheets връзка и Cell Format = Let n8n format = `RAW`) е записан като _versions/v2.json; в него таг липсваше и е добавен.

## 2026-10-13 - 09-job-application-screening v2
- Промяна: в Append to Google Sheet е добавена опция Cell Format = Let n8n format (`cellFormat: RAW`).
- Причина: телефони с водещ `+` се показваха като `#ERROR!` в таблицата (Sheets ги приемаше за формула); поправката е потвърдена от Здравко в UI.
- Засегнати нодове: Append to Google Sheet, Sticky Note. v1 е в _versions/.

## 2026-10-13 - 09-job-application-screening v1
- Промяна: първа доставка на JSON.
- Причина: ново домашно; скорингът е с Basic LLM Chain по искане на Здравко.
- Засегнати нодове: всички.
