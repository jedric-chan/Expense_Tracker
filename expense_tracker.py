def add_expense(expenses):
    """Add a new expense to the tracking system with validation"""
    while True:
        category = input("Enter category: ").strip()
        if not category:
            print("Category cannot be empty. Please try again.")
            continue
        
        amount = input("Enter amount: ").strip()
        try:
            amount = float(amount)
            if amount <= 0:
                print("Amount must be a positive number.")
                continue
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            continue
        
        while True:
            date = input("Enter date (YYYY-MM-DD): ").strip()
            if len(date) != 10 or date[4] != '-' or date[7] != '-':
                print("Invalid date format. Use YYYY-MM-DD.")
                continue
            try:
                year, month, day = map(int, date.split('-'))
                if not (1 <= month <= 12 and 1 <= day <= 31):
                    raise ValueError
            except ValueError:
                print("Invalid date values. Please check the date.")
                continue
            break
        
        expenses.append({
            'category': category,
            'amount': amount,
            'date': date
        })
        print("Expense added successfully!")
        break

def view_expenses(expenses):
    """Display all expenses in a formatted list"""
    if not expenses:
        print("\nNo expenses to display.")
        return
    
    print("\nAll Expenses:")
    print("-" * 40)
    for idx, expense in enumerate(expenses, 1):
        print(f"{idx}. Category: {expense['category']}")
        print(f"   Amount: ${expense['amount']:.2f}")
        print(f"   Date: {expense['date']}")
        print("-" * 40)

def filter_by_category(expenses):
    """Show expenses filtered by specific category"""
    if not expenses:
        print("\nNo expenses to filter.")
        return
    
    category = input("\nEnter category to filter: ").strip().lower()
    filtered = [expense for expense in expenses 
               if expense['category'].lower() == category]
    
    if not filtered:
        print(f"\nNo expenses found for category '{category}'.")
        return
    
    print(f"\nExpenses in '{category}':")
    print("-" * 40)
    for idx, expense in enumerate(filtered, 1):
        print(f"{idx}. Amount: ${expense['amount']:.2f}")
        print(f"   Date: {expense['date']}")
        print("-" * 40)

def calculate_total(expenses):
    """Calculate and display total of all expenses"""
    if not expenses:
        print("\nNo expenses to calculate.")
        return
    
    total = sum(expense['amount'] for expense in expenses)
    print(f"\nTotal Expenses: ${total:.2f}")

def delete_expenses(expenses):
    """Remove expenses by category and date"""
    if not expenses:
        print("\nNo expenses to delete.")
        return
    
    category = input("\nEnter category of expenses to delete: ").strip().lower()
    date = input("Enter date (YYYY-MM-DD) of expenses to delete: ").strip()
    
    initial_count = len(expenses)
    expenses[:] = [expense for expense in expenses 
                  if not (expense['category'].lower() == category 
                          and expense['date'] == date)]
    
    removed = initial_count - len(expenses)
    print(f"\nDeleted {removed} expense(s).")

def main_menu():
    """Display the main menu interface"""
    print("\nExpense Tracker Menu")
    print("=" * 25)
    print("1. Add New Expense")
    print("2. View All Expenses")
    print("3. Filter Expenses by Category")
    print("4. Calculate Total Expenses")
    print("5. Delete Expenses")
    print("6. Exit")
    return input("Enter your choice (1-6): ").strip()

def main():
    """Main program loop"""
    expenses = []
    
    while True:
        choice = main_menu()
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            filter_by_category(expenses)
        elif choice == '4':
            calculate_total(expenses)
        elif choice == '5':
            delete_expenses(expenses)
        elif choice == '6':
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1-6.")
            
        input("\nPress Enter to continue...")

main()
