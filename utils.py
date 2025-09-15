import csv
from datetime import datetime
from matplotlib import pyplot as plt
import numpy as np

import helpers

fieldnames = ['date', 'category', 'amount']

def get_file():
    while True:
        file_id = input("Enter your id: ")
        name = 'data/' + file_id + ".csv"
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

