# Data Table `support_tickets`

Създай таблицата в n8n (Data tables) преди първия тест, с име точно `support_tickets`. Всички колони са от тип string.

**Бърз старт:** импортирай `support_tickets_import.csv` (заглавен ред + един примерен ред `sample`, за да се изведат типовете като string). След импорта провери, че името на таблицата е `support_tickets` и че всички колони са String, и изтрий реда `sample`. Редът не пречи на потока (статусът му не е `pending_review`), но замърсява таблицата.

| Колона | Кой я пише | Съдържание |
|--------|-----------|------------|
| ticketId | WF1 Save Ticket As Pending | `TCK-yyyyMMdd-HHmmss-XXXX` |
| receivedAt | WF1 | ISO дата на получаване |
| customerName | WF1 | име или `Customer` |
| ticketText | WF1 | текст на тикета |
| sentimentAi | WF1 | оригиналната категория от Sentiment Analysis |
| department | WF1 | Sales / Technical / Billing / General |
| status | WF1, WF2 | `pending_review` -> `reviewed` -> `processed` или `failed` |
| sentimentFinal | WF2 Mark Reviewed | категорията след ревюто |
| reviewerNote | WF2 Mark Reviewed | бележка на ревюиращия |
| reviewedAt | WF2 Mark Reviewed | ISO дата на ревюто |
| processedAt | WF2 Mark Processed | ISO дата на обработката |
| errorNote | WF2 Mark Failed | съобщение за грешка (до 500 знака) |

`id`, `createdAt` и `updatedAt` са системни колони на Data Table (от паметта, непроверено с изпълнение) и не се създават.
