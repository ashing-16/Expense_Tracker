import os

class ExpenseTracker:
    def __init__(self, filename="expenses.txt"):
        self.filename = filename
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                for line in file:
                    date, description, amount = line.strip().split(',')
                    self.expenses.append({'date': date, 'description': description, 'amount': amount})


    def add_expense(self):
        date = input("Enter the date of the expense (YYYY-MM-DD): ")
        description = input("Enter a description of the expense: ")
        amount = float(input("Enter the amount of the expense: "))
        self.expenses.append({'date': date, 'description': description, 'amount': amount})
        print("Expense added successfully!")
    
    def clear_expenses(self):
        self.expenses = []
        with open(self.filename, 'w') as file:
            pass 
        print("All Expenses cleared from the file")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
        else:
            print("\nExpenses List:")
            print("Date       | Description         | Amount")
            print("------------------------------------------")
            for expense in self.expenses:
                print(f"{expense['date']} | {expense['description']} | {expense['amount']:}")

    def write_expenses_to_file(self):
        with open(self.filename, 'w') as file:
            for expense in self.expenses:
                file.write(f"{expense['date']},{expense['description']},{expense['amount']}\n")
        print("Expenses written to file successfully!")

def display_menu():
    print("\nExpense Tracker Menu:")
    print("a. Add expense")
    print("b. View expenses")
    print("c. Write expenses to file")
    print("d. Remove all Expenses")
    print("q. Quit")

tracker = ExpenseTracker()

while True:
    display_menu()
    choice = input("Choose an option: ")

    if choice == 'a':
        tracker.add_expense()
    elif choice == 'b':
        tracker.view_expenses()
    elif choice == 'c':
        tracker.write_expenses_to_file()
    elif choice == 'd':
        tracker.clear_expenses()
    elif choice == 'q':
        print("Exiting Expense Tracker.")
        break
    else:
        print("Invalid choice, please try again.")

