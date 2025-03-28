balance = 0
is_running = True

def show_balance():
    print(f"Your balance is ${balance}")

def withdraw():
    is_withdraw = True
    while is_withdraw:
        print("----Withdrawal----")
        amount = int(input("Enter amount to withdraw"))
        if amount > balance:
            print("Insufficient Funds")
            is_withdraw = False
            return 0
        elif amount < 0:
            print("Enter a valid number")
        else:
            is_withdraw = False
            return amount

def deposit():
    is_deposit = True
    while is_deposit:
        print("----Deposit----")
        amount = int(input("How much do you want to deposit?: "))
        if amount < 0:
            print("Enter a valid amount")
        else:
            is_deposit = False
            return amount

while is_running:
    print("----Titan Bank----")
    print("1. Show balance\n2. Withdrawal\n3. Deposit\n4. Exit")
    choice = int(input("Enter a number:"))

    if choice == 1:
        print(f"Your balance is ${balance}")
    elif choice == 2:
        balance -= withdraw(balance)
    elif choice == 3:
        balance += deposit(balance)
    elif choice == 4:
        is_running = False
    else: 
        print("Enter a valid option")
