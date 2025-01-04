class BankingSystem:
    def __init__(self):
        self.users = {}

    def create_account(self, username, password):
        if username in self.users:
            print("Account creation failed: Username already exists.")
            return

        self.users[username] = {"password": password, "balance": 0.0}
        print("Account created successfully!")

    def login(self, username, password):
        if username not in self.users:
            print("Login failed: Username does not exist.")
            return False

        if self.users[username]["password"] != password:
            print("Login failed: Incorrect password.")
            return False

        print("Login successful!")
        return True

    def deposit(self, username, amount):
        if amount <= 0:
            print("Deposit failed: Amount must be greater than 0.")
            return

        self.users[username]["balance"] += amount
        print(f"Deposit successful! New balance: {self.users[username]['balance']}")

    def withdraw(self, username, amount):
        if amount <= 0:
            print("Withdrawal failed: Amount must be greater than 0.")
            return

        if self.users[username]["balance"] < amount:
            print("Withdrawal failed: Insufficient balance.")
            return

        self.users[username]["balance"] -= amount
        print(f"Withdrawal successful! New balance: {self.users[username]['balance']}")

    def check_balance(self, username):
        print(f"Current balance: {self.users[username]['balance']}")

    def view_transactions(self, username):
        print("This simplified version does not include transaction history.")


def main():
    banking_system = BankingSystem()

    while True:
        print("\n=== Banking System ===")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            banking_system.create_account(username, password)

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if banking_system.login(username, password):
                while True:
                    print("\n--- Account Menu ---")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Logout")

                    account_choice = input("Enter your choice: ")

                    if account_choice == "1":
                        amount = float(input("Enter amount to deposit: "))
                        banking_system.deposit(username, amount)

                    elif account_choice == "2":
                        amount = float(input("Enter amount to withdraw: "))
                        banking_system.withdraw(username, amount)

                    elif account_choice == "3":
                        banking_system.check_balance(username)

                    elif account_choice == "4":
                        print("Logging out...")
                        break

                    else:
                        print("Invalid choice. Please try again.")

        elif choice == "3":
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

