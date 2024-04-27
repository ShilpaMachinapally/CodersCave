class ExpenseManager:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, payer, amount, *users):
        total_users = len(users) + 1
        individual_share = amount / total_users
        if payer not in self.expenses:
            self.expenses[payer] = 0
        self.expenses[payer] += amount
        for user in users:
            if user not in self.expenses:
                self.expenses[user] = 0
            self.expenses[user] -= individual_share

    def get_balance(self, user):
        if user in self.expenses:
            return self.expenses[user]
        else:
            return 0

    def settle_balance(self, user1, user2):
        if user1 in self.expenses and user2 in self.expenses:
            balance = self.expenses[user1] + self.expenses[user2]
            if balance < 0:
                print(f"{user1} owes {user2}: {abs(balance)}")
            elif balance > 0:
                print(f"{user2} owes {user1}: {balance}")
            else:
                print("No balance")
        else:
            print("User not found")

def main():
    expense_manager = ExpenseManager()

    while True:
        print("\n1. Add Expense")
        print("2. Check Balance")
        print("3. Settle Balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            payer = input("Enter the name of the payer: ")
            amount = float(input("Enter the amount: "))
            users = input("Enter the names of users (separated by comma): ").split(',')
            expense_manager.add_expense(payer, amount, *users)
            print("Expense added successfully!")
        elif choice == '2':
            user = input("Enter the name of the user: ")
            balance = expense_manager.get_balance(user)
            print(f"{user} has a balance of: {balance}")
        elif choice == '3':
            user1 = input("Enter the name of user 1: ")
            user2 = input("Enter the name of user 2: ")
            expense_manager.settle_balance(user1, user2)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
