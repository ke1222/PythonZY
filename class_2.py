class Account(object):
    def __init__(self,id = 0,balance = 100.0,annualInterestRate = 0.0):
        self._id = id
        self._balance = balance
        self._annualInterestRate = annualInterestRate
    @property #装饰器
    def id(self):
        return self._id  
    @id.setter #修改器
    def id(self,id1):
        self._id = id1
    
    @property
    def balance(self):
        return self._balance  
    @balance.setter
    def balance(self,balance1):
        self._balance = balance1
    
    @property
    def annualInterestRate(self):
        return self._annualInterestRate  
    @annualInterestRate.setter
    def annualInterestRate(self,annualInterestRate1):
        self._annualInterestRate = annualInterestRate1

    def getMonthlyInterestRate(self):#月利率
        MonthlyInterestRate = self.annualInterestRate/12/100
        return MonthlyInterestRate
    def getMonthlyInterest(self):#月利息
        Monthlylilv = self.getMonthlyInterestRate()
        Monthlylixi = self.balance * Monthlylilv
        return Monthlylixi
    def withdraw(self,money):#取钱
        if self._balance >= money:
            self._balance -= money
            print('您已成功取出:%.2f' % money)
            print('您的余额为:%.2f' % self._balance)
        else:
            print('您的余额不足')
            print('您的余额为:%.2f' % self._balance)
    def deposit(self,money):#存钱
        self._balance += money
        print('您已成功存入:%.2f' % money)
        print('您的余额为:%.2f' % self._balance)
if __name__ == "__main__":
    account = Account(id = 1122,balance=20000,annualInterestRate=4.5)
    print(account.getMonthlyInterest())
    account.withdraw(3000)
    
