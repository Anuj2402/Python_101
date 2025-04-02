#Python Banking Program 
print("Python Banking Program") #Prints the title of the program

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter amount to deposit: "))

    if amount < 0:
        print("Amount must be positive")
    else:
        return amount;
def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds")
    elif amount < 0:
        print("Amount must be positive")
    else:
        balance -= amount;
    
def main():
    balance = 0
    is_running = True

    while is_running:
        print("Banking Program")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Quit")

        choice = input("Enter choice:(1-4) ")
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            is_running = False
        else:
            print("Invalid choice")

    print("Thank you for banking with us")

if __name__ == "__main__":
    main()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------


