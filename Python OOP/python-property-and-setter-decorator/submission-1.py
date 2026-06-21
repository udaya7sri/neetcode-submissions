class BankAccount:
    def __init__(self, balance: int): 
        self.__balance = balance # Don't modify this line
        
    #Getter
    @property
    def balance(self)->int:
        return self.__balance
    
    #setter
    @balance.setter
    def balance(self, new_balance:int)->None:
        if new_balance >=0:
            return self.__new_balance
        else:
            print("Balance cannot be negative!")
        

# Don't modify the code below this line
account = BankAccount(1000)
print(account.balance)
account.balance = -100
