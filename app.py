from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime, timedelta

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('library.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']
        age = request.form['age']
        conn = get_db_connection()
        conn.execute('INSERT INTO Customers (Name, City, Age) VALUES (?, ?, ?)', (name, city, age))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_customer.html')

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        name = request.form['name']
        author = request.form['author']
        year_published = request.form['year_published']
        book_type = request.form['type']
        conn = get_db_connection()
        conn.execute('INSERT INTO Books (Name, Author, YearPublished, Type) VALUES (?, ?, ?, ?)', (name, author, year_published, book_type))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_book.html')

@app.route('/loan_book', methods=['GET', 'POST'])
def loan_book():
    if request.method == 'POST':
        cust_id = request.form['cust_id']
        book_id = request.form['book_id']
        loan_date = datetime.now()
        conn = get_db_connection()
        book = conn.execute('SELECT Type FROM Books WHERE Id = ?', (book_id,)).fetchone()
        if book:
            max_days = {1: 10, 2: 5, 3: 2}[book['Type']]
            return_date = loan_date + timedelta(days=max_days)
            conn.execute('INSERT INTO Loans (CustID, BookID, LoanDate, ReturnDate) VALUES (?, ?, ?, ?)', (cust_id, book_id, loan_date, return_date))
            conn.commit()
        conn.close()
        return redirect(url_for('index'))
    conn = get_db_connection()
    books = conn.execute('SELECT * FROM Books').fetchall()
    customers = conn.execute('SELECT * FROM Customers').fetchall()
    conn.close()
    return render_template('loan_book.html', books=books, customers=customers)

@app.route('/return_book', methods=['GET', 'POST'])
def return_book():
    if request.method == 'POST':
        cust_id = request.form['cust_id']
        book_id = request.form['book_id']
        conn = get_db_connection()
        conn.execute('DELETE FROM Loans WHERE CustID = ? AND BookID = ?', (cust_id, book_id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('return_book.html')

@app.route('/display_books')
def display_books():
    conn = get_db_connection()
    books = conn.execute('SELECT * FROM Books').fetchall()
    conn.close()
    return render_template('display_books.html', books=books)

@app.route('/display_customers')
def display_customers():
    conn = get_db_connection()
    customers = conn.execute('SELECT * FROM Customers').fetchall()
    conn.close()
    return render_template('display_customers.html', customers=customers)

@app.route('/display_loans')
def display_loans():
    conn = get_db_connection()
    loans = conn.execute('SELECT * FROM Loans').fetchall()
    conn.close()
    return render_template('display_loans.html', loans=loans)

@app.route('/display_late_loans')
def display_late_loans():
    conn = get_db_connection()
    late_loans = conn.execute('SELECT * FROM Loans WHERE ReturnDate < ?', (datetime.now(),)).fetchall()
    conn.close()
    return render_template('display_late_loans.html', loans=late_loans)

@app.route('/find_book', methods=['GET', 'POST'])
def find_book():
    if request.method == 'POST':
        name = request.form['name']
        conn = get_db_connection()
        books = conn.execute('SELECT * FROM Books WHERE Name LIKE ?', ('%' + name + '%',)).fetchall()
        conn.close()
        return render_template('display_books.html', books=books)
    return render_template('find_book.html')

@app.route('/find_customer', methods=['GET', 'POST'])
def find_customer():
    if request.method == 'POST':
        name = request.form['name']
        conn = get_db_connection()
        customers = conn.execute('SELECT * FROM Customers WHERE Name LIKE ?', ('%' + name + '%',)).fetchall()
        conn.close()
        return render_template('display_customers.html', customers=customers)
    return render_template('find_customer.html')

@app.route('/remove_book', methods=['POST'])
def remove_book():
    book_id = request.form['book_id']
    conn = get_db_connection()
    conn.execute('DELETE FROM Books WHERE Id = ?', (book_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('display_books'))

@app.route('/remove_customer', methods=['POST'])
def remove_customer():
    cust_id = request.form['cust_id']
    conn = get_db_connection()
    conn.execute('DELETE FROM Customers WHERE Id = ?', (cust_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('display_customers'))

if __name__ == '__main__':
    app.run(debug=True)
