#Atm Menu
#Pin Code Authentication
# 1.Check Balance
#2. Deposit Money
#3. Withdrow Money
#4.Exit
current_balance=1000
user_details={
    "ARPIT":1234,
    "ADARSH":5678,
    "JIGNESH":9101
}
max_attempts=3
attempts=0
locked_account={}
def authentication():
    global attempts,max_attempts,locked_account
    while True:
        user_name=input("Enter Username:").upper()
        if user_name in locked_account:
            print(f"Account is locked due to too many failed attempts. Please try again later.")
            exit()
        if user_name in user_details:
            while True:
                try:
                    user_pin = int(input("Enter Your Pin:"))
                    if user_details[user_name]==user_pin:
                        print("Successfully login")
                        attempts=0
                        return True
                    else:
                        attempts+=1
                        print(f"Invalid Pin.You have {max_attempts - attempts} attempts remaining.")
                        if attempts==max_attempts:
                            locked_account[user_name]=True
                            print("To many attempts Failed. Your Account is Locked")
                            break
                except ValueError:
                    print("Pin Only Numerical Value. Don't Enter Alphabets and Special Symbol")
        else:
            print("Username not found. Please try again.")


def check_balance():
    print(f"Your Current Balance is :Rs{current_balance:.2f}")

def deposit_money():
    global current_balance
    try:
        money=float(input("Enter the Amount to Deposit:Rs"))
        if money>0:
            current_balance+=money
            print(f"You Have Successfully Deposited:Rs{money:.2f}")
            check_balance()
        else:
            print("Invalid Deposit Amount. It must be greater than 0")
    except ValueError:
        print("Invalid input! Please enter a valid number (not letters or symbols).")

def withdraw_money():
    global current_balance
    try:
        money = float(input("Enter the Amount to Withdraw :Rs "))
        if money > 0 and money <= current_balance:
            current_balance-=money
            print(f"You Have Successfully Withdrawn:Rs{money:.2f}")
            check_balance()
        elif money > current_balance:
            print(f"Insufficient Funds. Your current balance is Rs {current_balance:.2f}.")
        else:
            print("Invalid Withdraw Amount. It must be greater than 0")
    except ValueError:
        print("Invalid input! Please enter a valid number (not letters or symbols).")
def menu():
    if authentication():
        while True:
            print("*"*50)
            print("\t\t\tWelcome to ATM")
            print("*"*50)
            print("\t1.Check Balance")
            print("\t2.Deposit Money")
            print("\t3.Withdraw Money")
            print("\t4.Exit")
            print("*"*50)
            try:
                ch=int(input("Enter Your Choice(1-4):"))
                match(ch):
                    case 1:
                        check_balance()
                    case 2:
                        deposit_money()
                    case 3:
                        withdraw_money()
                    case 4:
                        print("Thankyou for Using The ATM Goodbye!")
                        exit()
                    case _:
                        print("Your Selection Operation is Wrong--try again")
            except ValueError:
                 print("Invalid Input. Please Enter a Number between 1 to 4.  ")

menu()