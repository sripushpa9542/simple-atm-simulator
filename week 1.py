# Mini Project (W1): Simple ATM Simulator

users = {}
balances = {}


# 1. User Registration
def register():
    username = input("Enter your username: ")

    if username in users:
        print("Username already exists! Please login.")
        return

    pin = input("Create a 4-digit PIN: ")

    if len(pin) == 4 and pin.isdigit():
        users[username] = pin
        balances[username] = 5000
        print("Registration successful!")
        print("Your initial balance is Rs. 5000")
    else:
        print("Invalid PIN! PIN must contain exactly 4 digits.")


# 2. Check Balance
def check_balance(username):
    print("Current balance: Rs.", balances[username])


# 3. Deposit Money
def deposit(username):
    try:
        amount = float(input("Enter deposit amount: Rs. "))

        if amount > 0:
            balances[username] += amount
            print("Deposit successful!")
            print("Updated balance: Rs.", balances[username])
        else:
            print("Please enter a positive amount.")

    except ValueError:
        print("Invalid input! Please enter a number.")


# 4. Withdraw Money
def withdraw(username):
    try:
        amount = float(input("Enter withdrawal amount: Rs. "))

        if amount <= 0:
            print("Please enter a positive amount.")

        elif amount <= balances[username]:
            balances[username] -= amount
            print("Withdrawal successful!")
            print("Remaining balance: Rs.", balances[username])

        else:
            print("Insufficient balance!")

    except ValueError:
        print("Invalid input! Please enter a number.")


# 5. Main ATM Program
while True:
    print("\n===== SIMPLE ATM SIMULATOR =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register()

    elif choice == "2":
        username = input("Enter your username: ")
        pin = input("Enter your 4-digit PIN: ")

        if username in users and users[username] == pin:
            print("\nLogin successful!")

            # ATM Operations Menu
            while True:
                print("\n===== ATM MENU =====")
                print("1. Check Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Logout")

                option = input("Enter your choice: ")

                if option == "1":
                    check_balance(username)

                elif option == "2":
                    deposit(username)

                elif option == "3":
                    withdraw(username)

                elif option == "4":
                    print("Logged out successfully!")
                    break

                else:
                    print("Invalid choice! Please try again.")

        else:
            print("Invalid username or PIN!")

    elif choice == "3":
        print("Thank you for using our ATM!")
        break

    else:
        print("Invalid choice! Please try again.")