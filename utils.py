import csv
from datetime import datetime
from matplotlib import pyplot as plt
import numpy as np

fieldnames = ['date', 'category', 'amount']

def get_file():
    while True:
        file_id = input("Enter your id: ")
        name = file_id + ".csv"
        try:
            with open(name,"r"):
                return name
        except FileNotFoundError:
            new = input(f"File does not exist. Do you want to track one with id {file_id}? (y/n): ").lower()
            if new == 'y':
                initialise_file(name)
            elif new == 'n':
                pass
            else:
                print("Invalid response. Try again.!")

def initialise_file(name):
    """Initialises the csv file given as name by inserting headers"""

    # Define header values
    header = fieldnames

    # Opens File and initialises it with headers
    with open(name,'w',newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow(header)
    print(f"File {name} was created successfully")

def add_expense(amount, Category,filename):
    """opens the data file and appends the new expense with the date"""
    with open(filename, 'a',newline="\n") as file:
        expense_writer  = csv.DictWriter(file, fieldnames=fieldnames)
        expense_writer.writerow({'date':datetime.today().strftime("%d-%m-%y"),'category':Category,'amount':amount})

def view_expenses(filename):
    """opens the data file and outputs each row in it"""
    with open(filename,'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)

def show_total_expenses(filename, Category = None,):
    """Calculates and prints the total of all expenses by category,
    or if none are given, all records"""
    with open(filename,'r') as file:
        reader = csv.DictReader(file)
        expenses = 0
        for row in reader:
            if Category is not None:
                if row["category"] == Category:
                    expenses += float(row["amount"])
            else:
                expenses += float(row["amount"])
        print(f"Expenses: Rs.{expenses:.2f}")

def show_expense_report(filename):
    values = {}
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            values[row["category"]] = values[row["category"]] + float(row["amount"]) if row["category"] in values else float(row["amount"])

        x = np.array(list(values.keys()))
        y = np.array(list(values.values()))

        plt.bar(x,y,color="crimson")
        add_labels(x, y)
        plt.title(f'Expense Report of {filename}')
        plt.xlabel('Category')
        plt.ylabel('Amount (Rs.)')

        plt.tight_layout()
        plt.show()

def add_labels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha='center')