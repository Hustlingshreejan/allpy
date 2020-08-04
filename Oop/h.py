# class First:
#     def __init__(self):
#         print("Starting first")
#         super(First, self).__init__()
#         print("Existing first")
#     def printdetail(self):
#         print("Hello from First class")
# class Second:
#     def __init__(self):
#         print("Starting second")
#         super(Second, self).__init__()
#         print("Existing second")
# class Thrid(First,Second):
#     def __init__(self):
#         print("Starting third")
#         super(Thrid, self).__init__()
#         print("Existing third")
#     def printdetail(self):
#         print("My name is antony gonsalvis ")
#         super().printdetail()
# th =Thrid()
# th.printdetail()




class A:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print("this is of A area method")
        print(self.length*self.breadth)


class B():
    def __init__(self,length):
        self.length=length

    def area(self):
        d=self.length*3
        print(d)


class C(B,A):
    def __init__(self):
        super(B, self).__init__()

c=C()
c.area()

