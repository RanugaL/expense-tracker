import sqlite3

DB_NAME = 'tracker.db'

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    with get_connection() as conn:
        conn.execute('''
        CREATE TABLE IF NOT EXISTS expenses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL, 
            description TEXT
            )
        ''')
        conn.commit()

def add_expense(date,category,amount,desc=""):
    with get_connection() as conn:
        conn.execute('''
        INSERT INTO expenses (date,category,amount,description) 
        VALUES(?,?,?,?)
        ''', (date, category, amount, desc))
        conn.commit()

def get_all_expenses():
    with (get_connection() as conn):
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM expenses')
        return cursor.fetchall()
