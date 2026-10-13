# Solution plan - 09-job-application-screening

- Статус: `tested`
- Версия: v3 (v1, v2 са в _versions/)
- Workflow име: `Encorp | Homework | Week 03 | HW 02 | Job Application Screening`
- Таг: `encorp-homework`

## Изисквания
R1 Form Trigger с различни полета; R2 Information Extractor (name, email, phone, years, skills); R3 проверка 3+ години и поне 2 категории умения; R4 разделяне; R5 изход за подходящите; R6 (бонус) Google Sheet; R7 (бонус) скоринг с Basic LLM Chain или нодове (избрано: Basic LLM Chain).

## Схема
```
Form Trigger -> Config -> Compose Resume Text -> Information Extractor (+ OpenRouter Chat Model Extractor)
  -> Evaluate Candidate (Code) -> Is Qualified? (IF)
       true  -> Score Candidate (Basic LLM Chain + OpenRouter Chat Model Scoring + Structured Output Parser)
                -> Prepare Sheet Row -> Append to Google Sheet -> Qualified Candidates Output
       false -> Unqualified Candidates
```

## Нодове
| № | Нод | Защо | Покрива |
|---|-----|------|---------|
| 1 | Form Trigger | text, email, dropdown, radio, date, number, checkbox, textarea, file | R1 |
| 2 | Config (Set) | minYears=3, minSkillCategories=2, skillCategories (JSON) | R3 |
| 3 | Compose Resume Text (Set) | един `resumeText` за екстрактора, с днешна дата за периоди "до днес" | R2 |
| 4 | Information Extractor + OpenRouter Chat Model Extractor | схема name/email/phone/yearsOfExperience/skills | R2 |
| 5 | Evaluate Candidate (Code) | мапва свободните умения към категории детерминирано; `qualified` + `rejectionReason` | R3 |
| 6 | Is Qualified? (IF) | двупосочно разделяне | R4 |
| 7 | Score Candidate (Basic LLM Chain) + модел + Structured Output Parser | experienceScore 0-50, skillScore 0-50, summary | R7 |
| 8 | Prepare Sheet Row (Set) | плосък ред; totalScore и tier се смятат детерминирано (LLM смята само компонентите) | R6, R7 |
| 9 | Append to Google Sheet | запис на подходящите; Cell Format = Let n8n format (телефони с `+`) | R6 |
| 10 | Qualified Candidates Output (NoOp) | изход | R5 |
| 11 | Unqualified Candidates (NoOp) | изход за неподходящите | R4 |

## Тестов вход (v3)
Нодовете от Config нататък са същите като в тестваната v2. Преди Config: Manual Trigger -> Test Candidates (Code, 5 фиктивни кандидата, очакваният резултат е в `testCase`) -> Run Candidate Through Flow (Execute Workflow към самия workflow, Run once for each item) -> When Executed by Another Workflow (Accept all data) -> Config. Всеки кандидат е отделно под-изпълнение с един item, затова `.first()` в Evaluate Candidate и Prepare Sheet Row остава коректен. Loop Over Items е отхвърлен: изисква връзки от крайните нодове обратно към цикъла и би обработил повторно кандидат от формата.

## Допускания
- Работодателят търси .NET Web Developer; категории: Backend, Frontend, Data, Cloud/DevOps (ключови думи в Config).
- Years of experience не е поле във формата - извлича се от текста на CV.
- CV файлът е по избор и не се чете (PDF извън условието).
- Информационният екстрактор не пренася входните полета, затова Evaluate Candidate чете формата от `Compose Resume Text` с `.first()`.

## Credentials
OpenRouter (същият като в 08), Google Sheets OAuth2 (self-hosted: свой Google Cloud клиент и redirect URL от credential-а). Sheet с header от `test-data/sheet-header.csv`.

## Тестов план
Виж `test-data/test-resumes.md` (5 случая).

## Покритие
R1->1, R2->3,4, R3->2,5, R4->6,11, R5->10, R6->9, R7->7,8.
