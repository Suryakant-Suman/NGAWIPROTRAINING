from abc import ABC, abstractmethod
class Bank(ABC):
    @abstractmethod
    def interestRate(self):
        pass
    @abstractmethod
    def loan(self):
        pass

class customer(Bank):
    def interestRate(self):
        print("Interest Rate is 6%")

    def loan(self):
        print("Loan Rate is 5%")


t = customer()
t.interestRate()
t.loan()