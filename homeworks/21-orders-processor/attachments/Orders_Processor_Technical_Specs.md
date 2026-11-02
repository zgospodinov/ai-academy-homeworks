# Orders Processor AI System

A client (commercial sphere of your choice \- books, car parts, computers, smartphones, etc.) has asked you to assist them in creating an AI automation for processing the orders they make to suppliers in order to maintain their business running smoothly.

They need an AI automation system that will accept a user input with basic order data on which an AI Agent with access to the RAG database will draft an email and return the draft to the user. If the user approves it \- it has to be sent automatically to the designated email address and logged as a purchase order in a Google Sheet database. There must be an error workflow that will handle and notify the user for the errors that might occur.

## **The business requirements are:**

1. ### A **communication interface** that will be used to send the user input \- Form, Chat, Telegram/Discord/Slack Chatbot or combination;

2. ### **AI Agent** that will process the user input with the basic information and:

   1. Return a draft of the email if all the info that is needed is present in the input  
   2. Process an attached file (image) of the item that will be ordered and add it to the context of the request  
   3. Ask additional questions if no supplier is found in the RAG or information is missing  
   4. Continue with sending the email ONLY if the user explicitly confirms it

3. ### **RAG system** that will hold the suppliers information \- company, contact person, email address

4. ### **Error handler** that will track, log and trigger the main workflow again depending of the specification below

5. ### **Jailbreak protection** in case a third party tries 

## **Technical Specifications:**

1. ### Communication interface:

   1. Either a form trigger, chat trigger with public URL (maybe custom CSS to the trigger to be more visually pleasing?), Webhook (if there is a custom form) or some kind of messaging app integration \- Telegram, Slack, Discord, etc.

2. ### AI Assistant Agent

   1. The agent must process the input and:  
      1. Generate an email draft and return it to the user if all the information needed is present and the corresponding supplier is found in the RAG or  
      2. Ask additional questions if information is missing, there is more than one supplier with the same name or there is an issue (typo for example)  
      3. When the email draft is presented for confirmation there must be the following info: the email of the receiver, the body of the email, the email title and the image of the item (if present in the request)

3. ### RAG Vector Database

   1. The database will hold vectorised information about the suppliers \- contact person, company name, email address

4. ### Error handler 

   1. The error handler must send a message to you every time there is an error and include the error details  
   2. The main workflow must have a defense mechanism if the output ot the Agent is empty object \- if there is no output then there must be an error and the user message must be passed again for processing

5. ### Jailbreak prevention

   1. There must be at least one jailbreak prevention mechanism \- either on the input, output or both  
   2. The jailbreak attempts must be logged in a simple Google Sheet table to be tracked

## Basic workflow processing:

1. The client sends some basic information with parameters for making the purchase order. For example: “*Напиши имейл на Димитър и заяви 100 химикалки за книжарницата с доставка утре. Искай писмено потвърждение на поръчката.*” or “*Напиши имейл на Димитър и заяви 100 артикула като този от прикачената снимка за книжарницата с доставка утре. Искай писмено потвърждение на поръчката.*” (if an attachment with an image of a pen is passed with the query).  
2. The AI Agent checks the attached picture to determine the item (if there is a picture attached), then checks if all the required information is present \- company name or name of a person and/or company, item type, quantity, date of delivery and if there must be an email confirmation of the order.   
   1. The agent must search the vector database and find:  
      1. If only a person name is provided \- check if there is only one person and which is the company and obtain the email from the RAG  
      2. If there are more than one person with that name \- to obtain all of them and ask the user which one to use to send the email to  
      3. There is no such person or company \- the agent informs the user that there is no such person or company and to provide the email directly   
   2. If any info is missing in the user input:  
      1.  the agent must request it or omit it if the user asks to.   
      2. Such information is \- person/company, date of delivery, item/s, quantity, email confirmation  
   3. Date of delivery \- the date of delivery must always be the day of the week \+ date.  
      1. If the user provides only a date \- the agent must include the weekday in the email draft  
      2. If the user provides a weekday like “утре”, “следващият понеделник”, “след 5 дена”, the agent must provide the date also.  
   4. When the agent is ready and the request is processed \- the output must be an email draft with the following information: email title, email body, email recipient  
   5. The email draft must be either requested for correction or confirmed by the user to be send  
   6. If the user confirms \- send the email to the recipient  
3. In case there is an error or the agent outputs an empty object \- the error workflow must log the error and notify you and if the agent has outputted an empty object \- to pass the user query again for processing  
4. If there is a jailbreak attempt \- the attempt must be stopped and logged.  
5. If everything is in order and the user confirms that the email can be sent then the email (with attachment if there is any) must be sent to the supplier and the order must be logged in a Google Sheet with all the necessary information to be tracked further by the employees.

