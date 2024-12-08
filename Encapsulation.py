class BankAccount:
    def __init__(self, account_Number, Balance):
        self.__account_Number = account_Number
        self.__Balance = Balance
    
    def deposite(self, amount):
        self.__Balance += amount
        print(f"Deposited:{amount} New Balance:{self.__Balance}")

    def withdraw(self, amount):
        if amount < self.__Balance:
            self.__Balance -= amount
            print(f"withdraw:{amount} Remaining Balance:{self.__Balance}")
        else:
            print("Insufficient balance")

#create an object
account = BankAccount("123456", 1000)
account.deposite(500)
account.withdraw(300)