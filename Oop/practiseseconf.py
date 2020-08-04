from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def printacom(self):
        return True


class Rectangle(Shape):
    # def printacom(self):
    #     print("Hahaha")
    pass


a=Rectangle()
a.printacom()
