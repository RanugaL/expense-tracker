import csv
from datetime import datetime

def add_expense(amount, category):
    """opens the data file and appends the new expense with the date"""
    with open("data.csv", 'a',newline="\n") as file:
        expense_writer  = csv.writer(file)
        expense_writer.writerow([datetime.today().strftime("%d-%m-%y"),category,amount])

def view_expenses():
    """opens the data file and outputs each row in it"""
    with open("data.csv",'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def show_total_expenses(category = None):
    """Calculates and prints the total of all expenses by category,
    or if none are given, all records"""
    with open("data.csv",'r') as file:
        reader = csv.reader(file)
        expenses = 0
        for row in reader:
            if category is not None:
                if row[1] == category:
                    expenses += float(row[2])
            else:
                expenses += float(row[2])
        print(f"Expenses: Rs.{expenses:.2f}")
