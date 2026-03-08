A robust financial management system built using Object-Oriented Programming (OOP) principles. This application manages multiple budget categories, tracks inter-category transfers, and generates a visual percentage-spent-by-category chart to aid in strategic financial planning.
Technical Logic
The core of the application is the Category class, which encapsulates all financial ledger operations.
Ledger Encapsulation: Every transaction (deposit, withdrawal, or transfer) is stored as a dictionary within a list, ensuring a clear audit trail.
Transaction Validation:
Fund Checks: Prevents withdrawals or transfers if the balance is insufficient.
Description Handling: Automatically manages string truncation for clean visual formatting.
Visual Data Analysis:
Bar Chart Generation: A custom string-builder engine that calculates the percentage of total spending per category (rounded down to the nearest 10).
Horizontal Alignment: Dynamically aligns category names vertically below the chart, demonstrating advanced string manipulation.
Professional Use Case
This logic serves as the foundation for my State 10 Budgeting Ecosystem, which I use to manage equipment installments and ROI calculations for my industrial laundry venture in Abuja. It demonstrates my ability to translate complex financial constraints into clean, bug-free code.
Certification Context
This project is a requirement of the Scientific Computing with Python (v7) certification by freeCodeCamp. It verifies my competence in Class inheritance, method design, and data representation.
