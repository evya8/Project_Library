# Library Management System

This is a simple library management system built using Flask and SQLite. It allows you to manage books, customers, and book loans.

## Features

- Add a new customer
- Add a new book
- Loan a book
- Return a book
- Display all books
- Display all customers
- Display all loans
- Display late loans
- Find book by name
- Find customer by name
- Remove book
- Remove customer

## Prerequisites

- Python 3.6 or higher
- Flask
- SQLite

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/library-management-system.git
cd library-management-system
Create a virtual environment and activate it:
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install the required packages:
bash
Copy code
pip install Flask
Set up the database:
bash
Copy code
python
>>> from app import init_db
>>> init_db()
>>> exit()

## Running the Application
Start the Flask application:
bash
Copy code
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
Open your web browser and navigate to http://127.0.0.1:5000/.

## Project Structure
library-management-system/
│
├── app.py
├── database.db
├── schema.sql
├── static/
│   └── style.css
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── add_customer.html
│   ├── add_book.html
│   ├── loan_book.html
│   ├── return_book.html
│   ├── display_books.html
│   ├── display_customers.html
│   ├── display_loans.html
│   ├── display_late_loans.html
│   ├── find_book.html
│   └── find_customer.html
└── README.md

## Routes and Templates
/ - Home page (index.html)
/add_customer - Add a new customer (add_customer.html)
/add_book - Add a new book (add_book.html)
/loan_book - Loan a book (loan_book.html)
/return_book - Return a book (return_book.html)
/display_books - Display all books (display_books.html)
/display_customers - Display all customers (display_customers.html)
/display_loans - Display all loans (display_loans.html)
/display_late_loans - Display late loans (display_late_loans.html)
/find_book - Find a book by name (find_book.html)
/find_customer - Find a customer by name (find_customer.html)
/remove_book - Remove a book (part of display_books.html)
/remove_customer - Remove a customer (part of display_customers.html)

## Database Schema
The database contains three tables: Books, Customers, and Loans.

Books Table
Id (Primary Key)
Name
Author
YearPublished
Type (1: up to 10 days, 2: up to 5 days, 3: up to 2 days)

Customers Table
Id (Primary Key)
Name
City
Age

Loans Table
CustID (Foreign Key referencing Customers.Id)
BookID (Foreign Key referencing Books.Id)
LoanDate
ReturnDate

## License
This project is licensed under the MIT License. See the LICENSE file for details.