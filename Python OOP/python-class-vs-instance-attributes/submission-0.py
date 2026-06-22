class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts =0
    total_balance =0
    def __init__(self,name,balance) -> None:
        self.name = name
        self.balance = balance
        BankAccount.total_accounts+=1
        BankAccount.total_balance +=balance


# TODO: Create two accounts
BankAccount1 = BankAccount("Alice",1000)
BankAccount2 = BankAccount("Bob",2000)
# TODO: Print the information using the mentioned format
print(f"{BankAccount1.name}\'s balance: ${BankAccount1.balance}")
print(f"{BankAccount2.name}\'s balance: ${BankAccount2.balance}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")
