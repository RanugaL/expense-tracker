import csv
from datetime import datetime
from matplotlib import pyplot as plt
import numpy as np
import helpers,db


fieldnames = ['date', 'category', 'amount']

def get_username():
    while True:
        username = input("Enter your username: ").lower()

        if not db.user_exists(username):
            new = input(f"Username does not exist. Do you want to create profile for  {username}? (y/n): ").lower()
            if new == 'y':
                initialise_profile(username)
            elif new == 'n':
                pass
            else:
                print("Invalid response. Try again.!")
        else:
            return username

def initialise_profile(username):
    """Inserts a profile into the db with username given"""

    db.add_new_profile(username)
    print(f"Profile for {username} was created successfully")

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

def show_categoric_report(filename):
    values = {}
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            values[row["category"]] = values.get(row["category"],0.0) + float(row["amount"])

        x = np.array(list(values.keys()))
        y = np.array(list(values.values()))

        plt.bar(x,y,color="mediumorchid")
        helpers.add_labels(x,y)
        plt.title(f'Expense Report of {filename}')
        plt.xlabel('Category')
        plt.ylabel('Amount (Rs.)')

        # after plotting the data, format the labels
        current_values = plt.gca().get_yticks()
        plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in current_values])

        plt.show()

def show_timely_report(filename,year):
    month_totals = {1:0 ,2:0 ,3:0 ,4:0 ,5:0 ,6:0 ,7:0 ,8:0 ,9:0 ,10:0 ,11:0 ,12:0 }
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["date"][6:8] == str(year)[2:]:
                month = int(row["date"][3:5])
                month_totals[month] = month_totals.get(month) + float(row["amount"])

        x = np.array(list(["January","February","March","April","May","June","July","August","September","October","November","December"]))
        y = np.array(list(month_totals.values()))

        plt.bar(x, y, color="orange")
        helpers.add_labels(x, y)
        plt.title(f'Expense Report of {filename}')
        plt.xlabel('Category')
        plt.ylabel('Amount (Rs.)')

        # after plotting the data, format the labels
        current_values = plt.gca().get_yticks()
        plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in current_values])

        plt.show()

