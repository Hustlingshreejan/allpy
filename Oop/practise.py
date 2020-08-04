class Employee:
    no_of_leaves=10
    bonus=5600

    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printdetail(self):
        print(f"The name is {self.name} and the age is {self.age} and the gender is {self.gender} where the bonus is {self.bonus}")
    @classmethod
    def change_bonus(cls,new_bonus):
        cls.bonus=new_bonus

    @classmethod
    def dash(cls,string):
        params=string.split("-")
        print(params)
        return cls(params[0],params[1])




shreejan=Employee("shreejan_shrestha",21,"M")
shreeram=Employee("Shreeram_shrestha",52,"M")
sajana=Employee("Sajana_shrestha",51,"F")

# shreejan.printdetail()
# shreeram.printdetail()
# sajana.change_bonus(500000)
# print(shreeram.printdetail())
# shreejan.bonus=500
# shreejan.printdetail()
# shristi=Employee.dash("Shristi_Shakya-20")
# shristi.printdetail()

class Programmer(Employee):

    def printprog(self):
        print( f"The name of the programmer is {self.name} and the age of the programmer is {self.age} and the languages the programmer knows is ")


anish=Programmer("Anish_Shrestha",21,"M")
anish.printprog()
anish.printdetail()




