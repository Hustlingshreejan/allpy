#
# class Marks:
#
#     def __init__(self,m1,m2,m3):
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3
#     def average(self):
#         return sum([self.m1,self.m2,self.m3])//3
#
#
#
# class Smarks(Marks):
#
#     def __init__(self,num,snum):
#         super().__init__(10,20,30)
#         self.num=num
#         self.snum=snum
#         print("Hello from child class")
#
#     def sum(self):
#         # super().average()
#
#         print(sum([self.num,self.snum]))
#
#
#
# shreejan=Marks(1,1,1)
# # print(shreejan.m3)
# shree=Smarks(5,5)
# shree.sum()
# print(shree.m3)
#
# print(shree.average())

class Pycharm:

    def execute(self):
        print("Compiling")


class Laptop:

    def coding(self,ide):
        ide.execute()

ide=Pycharm()
l=Laptop()
l.coding(ide)