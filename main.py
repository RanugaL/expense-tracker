import utils

if __name__ == '__main__':
    interface = ["a - add expense",
                 "s - show expense report",
                 "t - show total expenses",
                 "c - show expenses for category",
                 "r - view expense report",
                 "q - Exit app"]
    while True:
        print()
        for row in interface:
            print(row)
        operation = input("Enter option: ").lower()
        if operation == 's':
            utils.view_expenses()
        elif operation == 'a':
            try:
                amount = float(input("Enter amount of expense: Rs."))
                category = input("Enter expense category: ").lower()
                utils.add_expense(amount, category)
            except TypeError:
                print("Value entered was not a float")

        elif operation == 't':
            utils.show_total_expenses()
        elif operation == 'c':
            category= input("Enter category: ").lower()
            utils.show_total_expenses(category)
        elif operation == 'r':
            utils.show_expense_report()
        elif operation == 'q':
            print("Exiting...")
            break