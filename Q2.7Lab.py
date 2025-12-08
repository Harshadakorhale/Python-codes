# 7. Write a function make_account(initial_balance) that returns two nested 
# functions: deposit(amount) and withdraw(amount). Use nonlocal to manage the 
# balance. Test by depositing 500 and withdrawing 200 from an account starting with 
# 1000. 

def make_account(initial_balance):
    balance = initial_balance

    def deposit(amount):
        nonlocal balance
        balance += amount
        print("Amount deposited successfully:", amount)
        print("Your remaining balance =", balance)
        return balance

    def withdraw(amount):
        nonlocal balance
        balance -= amount
        print("You withdrew $", amount)
        print("Your remaining balance $", balance)
        return balance

    return deposit, withdraw


deposit, withdraw = make_account(1000)
print(deposit(500))  
print(withdraw(200))  















