# 14-token-counter - Token Counter

- Седмица: 4
- Домашно: задача 1
- Статус: `tested`

## Условие (дословно)

Add an n8n Form Trigger that will accept user input (text) and LLM model (dropdown) - the models can be from Google Gemini and/or ChatGPT
If there are models from different providers - add logic to split them by the provider
Add Gemini and/or ChatGPT nodes with "Message a Model" operation
Disable the "Simplify Output" toggle in order to get the raw data from the model
When the LLM model generates a response - get the tokens data from the response
Add logic in order to determine how many input and output (completion) tokens the model generates and calculate the cost of them
Save all data in a Google Sheet where you can see which is the model, how many input, completion and total tokens have been generated and what is the cost of all of them.
When you run the workflow each time with the same prompt for different models you will have a comparison data for them based on price and token usage

## Изисквания

| № | Изискване | Тип |
|---|-----------|-----|
| R1 | Form Trigger с поле за текст и dropdown за модел (Gemini и/или ChatGPT) | задължително |
| R2 | При модели от различни доставчици - разделяне по доставчик | задължително (при >1 доставчик) |
| R3 | Gemini и/или OpenAI нод с операция "Message a Model" | задължително |
| R4 | "Simplify Output" изключен (суров отговор) | задължително |
| R5 | Извличане на token данните от отговора | задължително |
| R6 | Изчисляване на input / output (completion) токени и на цената им | задължително |
| R7 | Запис в Google Sheet: модел, input, completion, total токени, цена | задължително |
| R8 | Повторно пускане със същия prompt за различни модели дава сравнение по цена и токени | следствие от R7 |

## Отворени въпроси

| № | Въпрос / неяснота | Засяга | Тежест | Предложено допускане | Статус | Отговор |
|---|-------------------|--------|--------|----------------------|--------|---------|
| Q1 | Gemini и ChatGPT, или само един доставчик? В n8n няма Gemini (Google Gemini / PaLM) credential | R2, R3 | блокиращ | И двата; ще трябва да се създаде Gemini API key (безплатен от Google AI Studio) | answered | Да, и двата; Gemini credential ще се добави ръчно от Здравко |
| Q2 | Седмица и номер на задачата за името на workflow-а | име | блокиращ | Седмица 03, HW 07 | answered | Седмица 4, задача 1 |
| Q3 | Кои точно модели в dropdown-а и откъде са цените? | R1, R6 | неблокиращ | 2 от всеки доставчик, по един "евтин" и един "по-силен"; точният списък и цените (USD / 1M токена) се сверяват с официалните страници при изграждане | answered | ОК |
| Q4 | Нов Google Sheet или съществуващ? | R7 | неблокиращ | Нов документ "Token Counter" с една таблица, колони: timestamp, provider, model, prompt, input_tokens, completion_tokens, total_tokens, input_cost_usd, output_cost_usd, total_cost_usd | answered | ОК |
| Q5 | Gemini 2.5 връща "thinking" токени отделно от изходните, а се таксуват като изход | R6 | неблокиращ | completion = изходни + thinking токени за Gemini; за OpenAI completion_tokens вече включва reasoning | answered | ОК |
| Q6 | Цените в кода (константи в един Code/Set нод) или в Data Table / Sheet? | R6 | неблокиращ | Един Set/Code нод с таблица на цените - лесна промяна на едно място | answered | ОК |
