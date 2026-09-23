# 💰 Expense Tracker

A simple **Python Expense Tracker** that stores daily expenses in a CSV file and provides a spending summary with category-wise expenses.

## 📌 Features

* ➕ Add a new expense
* 📋 Display all saved expenses
* 📊 Calculate total spending
* 🗂️ Show category-wise spending
* 💾 Store expenses permanently in `expenses.csv`
* 🚪 Exit the program through a menu

## 🛠️ Technologies Used

* **Python**
* **CSV Module**
* **File Handling**
* **Functions**
* **Dictionary**
* **Loops & Conditional Statements**

## 📂 Project Structure

```text
Expense-Tracker/
│
├── expense_tracker.py
├── expenses.csv
└── README.md
```

## ▶️ How to Run

### 1. Install Python

Make sure Python is installed on your computer.

Check using:

```bash
python --version
```

### 2. Run the Program

Open the project folder in VS Code or Terminal and run:

```bash
python expense_tracker.py
```

## 📋 Menu Options

```text
===== EXPENSE TRACKER =====
1. Add Expense
2. Show Expenses
3. Spending Summary
4. Exit
```

### 1️⃣ Add Expense

Enter:

* Expense date
* Category
* Description
* Amount

Example:

```text
Enter expense date (DD-MM-YYYY): 23-09-2026
Enter category: Food
Enter description: Lunch
Enter amount: 150
```

The expense is automatically saved in `expenses.csv`.

### 2️⃣ Show Expenses

Displays all expenses stored in the CSV file.

Example:

```text
--- All Expenses ---
['23-09-2026', 'Food', 'Lunch', '150.0']
['23-09-2026', 'Travel', 'Bus', '50.0']
```

### 3️⃣ Spending Summary

Calculates:

* Total spending
* Category-wise spending

Example:

```text
--- Spending Summary ---
Total Spending: 200.0

Category-wise Spending:
Food : 150.0
Travel : 50.0
```

## 📄 CSV File

The program uses `expenses.csv` to store expense records.

Each record contains:

```text
Date, Category, Description, Amount
```

Example:

```text
23-09-2026,Food,Lunch,150
23-09-2026,Travel,Bus,50
```

## 🧠 Concepts Practiced

This project helps practice:

* `csv` module
* `open()` and file handling
* `csv.reader()`
* `csv.writer()`
* Functions
* `while` loop
* `if-elif-else`
* Dictionaries
* Exception handling with `try-except`
* Type conversion using `float()`

## 🎯 Purpose

The main purpose of this project is to practice **Python file handling and CSV data processing** by creating a simple real-world expense management application.

## 👨‍💻 Author

**Praval**

---

⭐ If you found this project useful, consider giving it a star!
