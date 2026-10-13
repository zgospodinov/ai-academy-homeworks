# Тестови кандидати (фиктивни данни)

Попълни формата през Test URL на Form Trigger. Останалите полета (position, salary, date...) са произволни.

## 1. Подходящ (очаквам qualified, 4 категории)
Name: Test Candidate One / Email: candidate1@example.com / Phone: +359 888 000 001
Resume text:
Senior .NET developer, 5 years of experience. 2021-2026 Acme Ltd: C#, ASP.NET Core Web API, Blazor, EF Core, SQL Server, Docker, Azure DevOps CI/CD. 2019-2021 Beta Ltd: C# and .NET desktop apps.

## 2. Неподходящ по опит (очаквам false: Experience 1 y < 3 y)
Name: Test Candidate Two / Email: candidate2@example.com / Phone: +359 888 000 002
Resume text:
Junior developer, 1 year of experience with C#, .NET and SQL.

## 3. Неподходящ по умения (очаквам false: Skill categories 0 < 2)
Name: Test Candidate Three / Email: candidate3@example.com / Phone: +359 888 000 003
Resume text:
6 years as a Java backend developer: Java, Spring Boot, Kafka, Oracle.

## 4. Граничен: опит само като периоди
Resume text: "2022-present: C# developer with ASP.NET Core and Azure. 2020-2022: SQL developer." Очаквам около 4-6 г. (днес 2026-10-13); виж как екстракторът смята.

## 5. Празни данни от екстрактора
Resume text: "I love coding." Очаквам yearsOfExperience 0 и неподходящ.
