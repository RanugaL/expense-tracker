import sqlite3

DB_NAME = 'tracker.db'

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('PRAGMA foreign_keys = ON;')

        c.execute('''
        CREATE TABLE IF NOT EXISTS profile(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL 
            )
        ''')

        c.execute('''
        CREATE TABLE IF NOT EXISTS expenses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL, 
            description TEXT, 
            FOREIGN KEY(user_id) REFERENCES profile(id)
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

def get_all_usernames():
    with (get_connection() as conn):
        cursor = conn.cursor()
        cursor.execute('SELECT username FROM profile')
        return cursor.fetchall()

def user_exists(username):
    with (get_connection() as conn):
        cursor = conn.cursor()
        cursor.execute('SELECT username FROM profile WHERE username = ?',username)
        return cursor.fetchall()