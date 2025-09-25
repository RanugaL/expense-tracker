from tkinter.font import names

import utils, db

def menu():
    print("1 - Add new expense")
    print("2 - List all expenses")
    print("3 - Delete an Expense")
    print("4 - View expense report (chart)")
    print("0 - Exit App")
    return input("Choose an action: ")


def main():

    # initialise database and get username
    db.init_db()
    user_data = utils.get_user()
    user_id = user_data[0][0]
    username = user_data[0][1]
    print(user_data)

    while True:

        # Get action from menu func
        option = menu() #

        # Perform selected action

        if option == '1': # Add new expense

            # Get and validate values for the expense
            amount: float  = utils.input_amount("Enter expense amount: Rs.")
            # returns -1 if invalid type, -2 if amount is negative else returns amount
            if amount == -1:
                print("❌ Invalid Input for amount")
                continue
            elif amount == -2:
                print("❌ amount cant be negative")
                continue
            category: str = input("Enter category of expense: ")
            desc: str = input("Enter a description for the expense: ")
            date = utils.get_today()

            # Add expense to database with user-id
            db.add_expense(user_id, date,category, amount,desc)
            print("✅ Expense added!")

        elif option == '2':
            # Prints each expense for a certain user
            print("-------------------")
            print(f"Expenses of {username}")
            data_query = db.get_all_expenses(user_id)
            for row in data_query:
                print(f"{row[0]}|{row[2]}|{row[3]}|{row[4]}|{row[5]}")
            print("-------------------")
        elif option == '3':
            pass

        elif option == '4':
            # Plots a chart of total expenses for each category
            data_query = db.get_expenses_grouped_by_category(user_id)

        elif option == '0':
            print("Exiting...")
            break

if __name__ == '__main__':
    main()