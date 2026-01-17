from abc import ABC, abstractmethod
class shape(ABC):
    def mtd(self):
        print("Normal method called")

    @abstractmethod
    def area(self):
        pass

class Rectangle(shape):
    def area(self):
        print("Rectangle method called")


r = Rectangle()
r.area()
r.mtd()