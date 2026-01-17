from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def salary(self):
        pass

class manager(Employee):
    def salary(self):
        print(self.name, "Salary is 50000")

t = manager("Ravi")
t.salary()