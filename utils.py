from datetime import datetime
import db

def get_user():
    while True:
        username = input("Enter your username: ").lower()

        user_query = db.get_profile(username)
        if not user_query :
            new = input(f"Username does not exist. Do you want to create profile for  {username}? (y/n): ").lower()
            if new == 'y':
                db.add_new_profile(username)
                print(f"Profile for {username} was created successfully")
            elif new == 'n':
                pass
            else:
                print("Invalid response. Try again.!")
        else:
            return user_query

def input_amount(prompt):
    amount = input(prompt)
    try:
        amount = float(amount)
    except (TypeError, ValueError):
        return -1
    else :
        if amount > 0 :
            return amount
        else:
            return -2


def get_today():
    return datetime.today().strftime("%d-%m-%y")

def get_year(prompt):
    year = input(prompt)
    try:
        year = int(year)
    except (TypeError, ValueError):
        return -1
    else:
        if not (1950 < year < 2100):
            return -2
        else:
            return str(year)
