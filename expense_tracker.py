# Expense Tracker using Python
import csv
import os
from datetime import datetime

# File for noting expenses
FILE_NAME = 'expenses.csv'

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Date', 'Amount', 'Category','Description'])

# Add Expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD) or leave blank for today:").strip()
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    else:
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            print("Invalid date format. Use YYY-MM-DD.")
            return
        try:
            amount = float(input("Enter amount:"))
        except ValueError:
            print("Amount must be a number.")
            return
        
        category = input("Enter category(eg., Food, Transport):").strip()
        description = input("Enter description:").strip()

        expenses = read_expenses()
        new_id = 1 if not expenses else int(expenses[-1][0])+1

        with open(FILE_NAME, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([new_id, date, amount, category, description])
        print("Expense added successfully!")

# Read expense
def read_expenses():
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader) #skip header
        return list(reader)
    
# View expense
def view_expenses():
    expenses = read_expenses()
    if not expenses:
        print("No expenses found.")
        return
    
    print(f"{'ID':<5}{'Date':<12}{'Ampunt':<10}{'Category':<15}Description")
    print("-"*60)
    for exp in expenses:
        print(f"{exp[0]:<5}{exp[1]:<12}{exp[2]:<10}{exp[3]:<15}{exp[4]}")

# delete expense
def delete_expense():
    try:
        del_id = input("Enter expense ID to delete:").strip()
        expenses = read_expenses()
        new_expenses = [exp for exp in expenses if exp[0] !=del_id]
        if len(new_expenses) == len(expenses):
            print("Expense ID not found.")
            return
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Date', 'Amount', 'Category', 'Description'])
            writer.wrtierows(new_expenses)
        print("Expense deleted successfully!")
    except Exception as e:
        print("Error deleting expense:", e)

def main_menu():
    initialize_file()
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Delete Expense")
        print("4. Exit")

        choice = input ("Enter your choice:").strip()

        if choice == '1':
            add_expense()
        elif choice =='2':
            view_expenses()
        elif choice =='3':
            delete_expense()
        elif choice =='4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1-4.")

if __name__=="__main__":
    main_menu()        