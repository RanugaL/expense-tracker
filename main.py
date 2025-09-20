import utils, db

if __name__ == '__main__':
    interface = ["n - add new expense",
                 "l - list expense records",
                 "t - show total expenses",
                 "c - show expenses for category",
                 "r - view expense report",
                 "q - Exit app"]

    database = db.init_db()

    while True:
        print()
        for row in interface:
            print(row)
        operation = input("Enter option: ").lower()
        if operation == 'l':
            utils.view_expenses(filename)
        elif operation == 'n':
            try:
                amount = float(input("Enter amount of expense: Rs."))
                category = input("Enter expense category: ").lower()
                utils.add_expense(amount, category,filename)
            except TypeError:
                print("Value entered was not a float")

        elif operation == 't':
            utils.show_total_expenses(filename)
        elif operation == 'c':
            category= input("Enter category: ").lower()
            utils.show_total_expenses(filename, category)
        elif operation == 'r':
            print("1 - Categoric Report\n" + "2 - Monthly Report")
            report_choice = input("Enter your choice (1/2): ")
            if report_choice == "1":
                utils.show_categoric_report(filename)
            else:
                year = int(input("Enter your desired year: "))
                utils.show_timely_report(filename, year)
        elif operation == 'q':
            print("Exiting...")
            break