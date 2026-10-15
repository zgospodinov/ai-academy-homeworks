# Changelog - 11-meeting-notes-summariser

## 2026-10-15 - v2 (потвърждение)
- Промяна: няма промяна във файла. Здравко потвърди, че главният поток е работил още във v1; статус -> tested.
- Бележка: изразът за четене на текста в Label Department Summaries и Attach Date To Summary във v2 е превантивен (изходът на chain-а е обект), не поправка на счупен нод. Какво точно е записвал Set във v1 в полетата `summary` / `generalSummary`, не е проверено.
- Засегнати нодове: няма.

## 2026-10-15 - v2 (бонус данни)
- Промяна: `comparison.md` допълнен с времена и токени за Stuff и Map Reduce, броя извиквания от логовете (Stuff 1, Refine 14, Map Reduce 1) и поправена оценка (14 chunk-а, не 13); времето на Refine е изведено от стартовите часове.
- Причина: данни от Здравко.
- Засегнати нодове: няма.

## 2026-10-14 - v2
- Промяна: `Build Comparison` чете текста от `response.text` / `response.output_text`; `Label Department Summaries` и `Attach Date To Summary` четат `$json.response?.text ?? $json.response?.output_text ?? $json.response ?? $json.output`; Sticky Note отбелязва v2.
- Причина: резултатът от сравнението на Здравко показа, че изходът на Summarization Chain е обект (`{text}` за Stuff / Map Reduce, `{output_text}` за Refine), не низ: `summaryChars` липсваше, `summary` беше обект. Set нодовете с тип string в основния поток разчитаха на същото предположение.
- Засегнати нодове: Build Comparison, Label Department Summaries, Attach Date To Summary, Sticky Note. Останалото е непроменено спрямо v1 (v1 е в `_versions/`).

## 2026-10-14 - v1
- Промяна: нов домашен (седмица 3, задача 4) - Schedule Trigger, Code с 4 бележки, две Summarization Chain с Map Reduce (по среща и общо), Date & Time + Edit за датата, бонус клон Stuff / Refine / Map Reduce.
- Причина: ново домашно; планът е одобрен от Здравко.
- Засегнати нодове: всички (нов).
