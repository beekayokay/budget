from budget import Budget

budget = Budget()
budget.read_config()
last_paid = budget.last_paid
mint_analysis = budget.mint_analysis


def print_menu():
    print(30 * '-', 'MENU', 30 * '-')
    print('0. Exit')
    print('1. Default Actions')
    print('2. Print Budget Again')
    print('3. Generate Bills')
    print(66 * '-')


loop = True

budget.read_csv(last_paid=last_paid, mint_analysis=mint_analysis)
budget.analyze_budget(mint=budget.mint, mint_analysis=mint_analysis)

while loop:
    print_menu()
    choice = input('Enter your choice: ')

    if choice == str(0):
        print(66 * '=')
        print('Peace bro')
        print(66 * '=')
        break
    elif choice == str(1):
        print(66 * '=')
        budget.read_csv(last_paid=last_paid, mint_analysis=mint_analysis)
        budget.analyze_budget(mint=budget.mint, mint_analysis=mint_analysis)
        print(budget.budget_analysis.to_markdown())
        print(66 * '=')
    elif choice == str(2):
        print(66 * '=')
        print(budget.budget_analysis.to_markdown())
        print(66 * '=')
    elif choice == str(3):
        budget.generate_bill()
        print(66 * '=')
        print(budget.bills.to_markdown())
        print(budget.last_7_df.to_markdown())
        print(budget.next_21_df.to_markdown())
        print(66 * '=')
    else:
        print(66 * '=')
        print('You picked a wrong value bruh, try again')
        print(66 * '=')
