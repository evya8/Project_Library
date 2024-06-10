import sqlite3

conn = sqlite3.connect('library.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS Books (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Author TEXT NOT NULL,
    YearPublished INTEGER NOT NULL,
    Type INTEGER NOT NULL CHECK (Type IN (1, 2, 3))
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS Customers (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    City TEXT NOT NULL,
    Age INTEGER NOT NULL
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS Loans (
    CustID INTEGER NOT NULL,
    BookID INTEGER NOT NULL,
    LoanDate TEXT NOT NULL,
    ReturnDate TEXT,
    FOREIGN KEY (CustID) REFERENCES Customers (Id),
    FOREIGN KEY (BookID) REFERENCES Books (Id),
    PRIMARY KEY (CustID, BookID)
)
''')

conn.commit()
conn.close()
