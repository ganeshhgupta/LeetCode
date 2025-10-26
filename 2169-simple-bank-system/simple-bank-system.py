class Bank:

    def __init__(self, balance: List[int]):
        self.bal = balance
        self.n = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        
        if max(account1, account2) > self.n or min(account1, account2) < 1 or self.bal[account1 - 1] < money:
            return False

        self.bal[account1 - 1] -= money
        self.bal[account2 - 1] += money
        return True


    def deposit(self, account: int, money: int) -> bool:

        if account > self.n or account < 1:
            return False

        self.bal[account - 1] += money
        return True


    def withdraw(self, account: int, money: int) -> bool:
        
        if account > self.n or self.bal[account - 1] < money:
            return False

        else:
            self.bal[account - 1] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)