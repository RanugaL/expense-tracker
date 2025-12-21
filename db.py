import sqlite3

# DATABASE INITIALISATION
DB_NAME = 'tracker.db'


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    """create necessary tables and initialises the database"""

    with get_connection() as conn:
        c = conn.cursor()
        c.execute('PRAGMA foreign_keys = ON;')

        c.execute('''
        CREATE TABLE IF NOT EXISTS profile(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE 
            )
        ''')

        c.execute('''
        CREATE TABLE IF NOT EXISTS expenses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            userid INTEGER NOT NULL,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL, 
            description TEXT, 
            FOREIGN KEY(userid) REFERENCES profile(id)
            )
        ''')

        conn.commit()


# TABLE: EXPENSES
def add_expense(user_id, date, category, amount, desc=""):
    with get_connection() as conn:
        conn.execute('''
        INSERT INTO expenses (userid,date,category,amount,description) 
        VALUES(?,?,?,?,?)
        ''', (user_id, date, category, amount, desc))
        conn.commit()


def get_all_expenses(user_id):
    with (get_connection() as conn):
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM expenses WHERE userid = ?', (user_id,))
        return cursor.fetchall()


def get_latest_expense(user_id):
    with (get_connection() as conn):
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM expenses WHERE userid = ? ORDER BY id DESC LIMIT 1', (user_id,))
        return cursor.fetchall()


def get_expense_by_id(expense_id, user_id):
    with (get_connection() as conn):
        cursor = conn.execute('SELECT * FROM expenses WHERE userid = ?  AND id = ?', (user_id, expense_id))



def delete_expense_by_id(expense_id, user_id):
    with (get_connection() as conn):
        conn.execute('DELETE FROM expenses WHERE userid = ? AND id = ? ', (user_id, expense_id))
        conn.commit()


def get_expenses_grouped_by_category(user_id):
    with(get_connection() as conn):
        cursor = conn.cursor()
        cursor.execute('''
        SELECT category, SUM(amount) FROM expenses
        WHERE userid = ?
        GROUP BY category
        ''', (user_id,))
        return cursor.fetchall()


def get_expenses_grouped_by_month(user_id,year):
    with(get_connection() as conn):
        cursor = conn.cursor()
        cursor.execute('''
        SELECT STRFTIME('%m', date) AS month, SUM(amount) as total FROM expenses
        WHERE userid = ?
        AND STRFTIME('%Y', date) = ? 
        GROUP BY month
        ''', (user_id,year))
        return cursor.fetchall()


# TABLE: PROFILE
def add_new_profile(username):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO profile (username) VALUES (?)', (username,))
        conn.commit()


def get_profile(username):
    with (get_connection() as conn):
        cursor = conn.cursor()
        cursor.execute('SELECT id,username FROM profile WHERE username = ?', (username,))
        return cursor.fetchall()


def get_all_usernames():
    with (get_connection() as conn):
        cursor = conn.cursor()
        cursor.execute('SELECT username FROM profile')
        return cursor.fetchall()
