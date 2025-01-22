from expense import Expense

def main():
    print(f"Running Expense Tracker!")
    expense_file_path="expenses.csv"
    budget=5000

    # Get user input for expense.
    expense=get_user_expense()

    # Write their expense into file.
    save_expense_to_file(expense,expense_file_path)

    # Read file and summarize expense.
    summarize_expenses(expense_file_path,budget)

def get_user_expense():
    print(f"Getting user expenses ")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    print(f"you have entered {expense_name},{expense_amount}")

    expense_categories=["Food","work","Home","Fun","Transport","other"]

    while True:
        print("Select a category: ")
        for i,category_name in enumerate(expense_categories):
            print(f"{i+1}.{category_name}")
            
        value_range=f"[1-{len(expense_categories)}]"
        selected_index=int(input(f"Enter a category number {value_range}: "))-1

        if selected_index in range(len(expense_categories)):
            selected_category=expense_categories[selected_index]
            new_expense=Expense(name=expense_name,category=selected_category,amount=expense_amount)
            return new_expense
        else:
            print("Invalid Category. Please try again! ")

def save_expense_to_file(expense: Expense,expense_file_path):
    print(f"Saving user expense: {expense} to {expense_file_path}")
    with open(expense_file_path,"a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")

def summarize_expenses(expense_file_path,budget):
    print("Summarizing user expenses")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:
        lines=f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category=line.strip().split(",")
            line_expense=Expense(name=expense_name, amount=float(expense_amount), category=expense_category)
            expenses.append(line_expense)

    amount_by_category={}
    for i in expenses:
        key=i.category
        if key in amount_by_category:
            amount_by_category[key]+=i.amount
        else:
            amount_by_category[key]=i.amount

    print("Expenses by Category : ")
    for key,amount in amount_by_category.items():
        print(f" {key}: {amount:.2f} rs")
    
    total_spent=sum([x.amount for x in expenses])
    print(f"You have spent {total_spent:.2f}rs this month !")

    remaining_budget= budget - total_spent
    print(f"Budget remaining : {remaining_budget:.2f}rs ")



if __name__ =="__main__":
    main()