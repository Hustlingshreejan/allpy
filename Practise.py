# # # # # tut 6
# # # # # print("This is a calculator")
# # # # # firstnum = int(input("Your first num"))
# # # # # secondnum = int(input("Your second num"))
# # # # # print("The addition of two numbers is", firstnum+secondnum)
# # # # #
# # # # # s="my name is shreejan shrestha"
# # # # # # print(len(s))
# # # # # # print(s[0:7:1])
# # # # # print(s.capitalize())
# # # # # print(s.upper())
# # # # # print(s.isalnum())
# # # # # x=s.encode()
# # # # # print(x)
# # # # # print(s.center(20))
# # # #
# # # # # listt=[1,2,3,4]
# # # # # # print(listt[0:3:-1])
# # # # # listt.append(11)
# # # # # print(listt)
# # # # #
# # # # # listt.insert(2, 100)
# # # # # print(listt)
# # # # #
# # # # # listt[3]=4
# # # # # print(listt)
# # # # #
# # # # # listt.pop()
# # # # # print(listt)
# # # # #
# # # # # listt.append(4)
# # # # # print(listt)
# # # # #
# # # # # listt.insert(1,4)
# # # # # print(listt)
# # # # #
# # # # # listt.remove(4)
# # # # # print(listt)
# # # # #
# # # # # del listt[1]
# # # # # print(listt)
# # # # #
# # # # # list2=[2,3,5,6,7]
# # # # # print(list2)
# # # # # print(listt)
# # # # # listt.extend(listt)
# # # # # print(listt)
# # # # #
# # # # # l=[1,1,2,3,4,4]
# # # # # print(set(l))
# # # #
# # # #
# # # # # a={"Shreejan":"Son","Shreeram":"Daddy"}
# # # # # print(a)
# # # # # print(a.get("Shreeram"))
# # # # # a.update({"Sajana":"Mummy"})
# # # # # print(a)
# # # # # del a["Shreejan"]
# # # # # print(a)
# # # # #
# # # # # a.update({"Puntu":{"daddy":"bhukku","Mummy":"chinku","shreejan":"laley"}})
# # # # # print(a)
# # # # # print(a["Puntu"]["daddy"])
# # # #
# # # # # ll=[1,2,3,4,[1,2,3]]
# # # # # print(ll[4][1])
# # # # # print(ll.__getitem__(2))
# # # #
# # # # #######################################################################################################################
# # # #
# # # # # print("This is a dictionary")
# # # # # d={"Egg":"Anda","Rice":"Bhaat","Meat":"masu"}
# # # # # user=input("What you want to search:")
# # # # # for keys in d.keys():
# # # # #     if user == keys:
# # # # #         a=d.get(user)
# # # # #         print("The meaning of word ", user, "is", a)
# # # # #         break
# # # # #
# # # # #     elif user not in keys:
# # # # #         a=d.get(user,"Not Found")
# # # # #         print("The word",user,a)
# # # #
# # # # ########################################################################################################################
# # # #
# # # #
# # # # # lis=[1,2,3,4]
# # # # # print(max(lis))
# # # #
# # # #
# # # # # print('Shreejan\'s "laptop\n" is dell',end=" ")
# # # # # print("Hello world\t" "HI")
# # # # #
# # # # # print('c\doc\navin')
# # # #
# # # # # l=[1,2,3,4]
# # # # # l.pop(2)
# # # # # print(l)
# # # # #
# # # # # del l[2]
# # # # # print(l)
# # # # #
# # # # # l1=[1,2,3,4,3]
# # # # # l2=[4,5,6,3]
# # # # #
# # # # #
# # # # # merge=dict(zip(l1,l2))
# # # # # print(merge)
# # # #
# # # # # l1.extend(l2)
# # # # # print(l1)
# # # # #
# # # # # l1.extend([7,8,9])
# # # # # print(l1)
# # # #
# # # # # help()
# # # #
# # # # # a=10
# # # # # print(id(a))
# # # #
# # # # # t=(1,2,3,'shreejan')
# # # # # print(t[3])
# # # # # print(bin(12))
# # # # #
# # # # # a = bin(25)
# # # # # print(a)
# # # #
# # # #
# # # # # user= input("Enter any character:")[0]
# # # # # print(user)
# # # # #
# # # # # import math
# # # # # user=int(input("Cube of??"))
# # # # # # print(user**3)
# # # # #
# # # # # print(int(math.pow(user,3)))
# # # #
# # # #
# # # # # user= int(input("Enter your age: "))
# # # # # if user>18 and user< 90:
# # # # #     print("You can drive")
# # # # # elif user <18 and user>1:
# # # # #     print("You are too small to drive")
# # # # # elif user <1 or user>90:
# # # # #     print("Dead end")
# # # # # else:
# # # # #     print("We have to see you physically")
# # # #
# # # # # listt=[['sohan','r'],['shreejan','s']]
# # # # # print(listt)
# # # # #
# # # # # for name, alpha in listt:
# # # # #     print(name, 'and', alpha)
# # # # #
# # # # # dictt=dict(listt)
# # # # # print(dictt)
# # # # # for name, alll in dictt.items():
# # # # #     print("name is",name,'and character is',alll)
# # # # #
# # # # # for key in dictt.items():
# # # # #     print(key)
# # # #
# # # # # userdetail={ 111:{'username':'shreejan','email':'shreejan@gmai.com'},222:{'username':'shree','email':'shree@gmail.com'}}
# # # # #
# # # # # admin=int(input("Type the userid to get the detail: "))
# # # # # detail=userdetail.get(admin)
# # # # # print(detail)
# # # # #
# # # # # for key,value in detail.items():
# # # # #     print("For the id 111 the",key,"is",value)
# # # #
# # # #
# # # #
# # # # # userdetails={'usernames': ['Shreejan', 'shree', 'sunil'], 'email': ['shreejan@gmai.com', 'shree@gmail.com']}
# # # # # for key, value in userdetails.items():
# # # # #     if key == 'usernames':
# # # # #         # print(value)
# # # # #         for name in value:
# # # # #             print("Facebook user",name)
# # # #
# # # # # l=[1,333,2,3,'shreejan',33]
# # # # # print(len(l))
# # # # # # for values in l:
# # # # # #     # print(values)
# # # # # #     if str(values).isnumeric() and values>6:
# # # # # #         print(values)
# # # # #
# # # # # i=1
# # # # # while i<=len(l):
# # # # #     print("Jay Nepal")
# # # # #     i+=1
# # # #
# # # # #
# # # # # i=0
# # # # # while(True):
# # # # #     user=int(input("num:"))
# # # # #     if user <=100:
# # # # #         print(user)
# # # # #         continue
# # # # #     else:
# # # # #         print("You have entered the number bigger than 100")
# # # # #         break
# # # #
# # # # # a=2.9
# # # # # print(a.__floordiv__(a))
# # # # # a.ceil
# # # #
# # # # # a= True
# # # # # b=False
# # # # # print(a or b)
# # # #
# # # # # import math
# # # # # b=2.9
# # # # # c=1.1
# # # # # print(math.floor(b))
# # # # # print(math.ceil(c))
# # # #
# # # # # i=1
# # # # # while i in range(101):
# # # # #     if i % 3 != 0 and i % 5 !=0:
# # # # #         print(i)
# # # # #     i +=1
# # # # #
# # # #
# # # # # i=1
# # # # # while i<=5:
# # # # #
# # # # #     print("#",end=" ")
# # # # #     j = 1
# # # # #     while j<=5:
# # # # #         print("*", end="")
# # # # #         j+=1
# # # # #
# # # # #     i+=1
# # # # #     print()
# # # #
# # # #
# # # # # i=1
# # # # # while i in range(i,6):
# # # # #     print('#',end=" ")
# # # # #     j = 1
# # # # #
# # # # #     while j in range(j,6):
# # # # #         print("*",end=" ")
# # # # #         j+=1
# # # # #     i+=1
# # # # #     print()
# # # #
# # # # # i=1
# # # # # while (True):
# # # # #     a= i**2
# # # # #     if a <501:
# # # # #         print(a)
# # # # #     else:
# # # # #         break
# # # # #     i+=1
# # # # #
# # # # #  # for i in range(1,51):
# # # # # #     a=i**2
# # # # # #     if a <50:
# # # # # #         print(a)
# # # # # #     else:
# # # # # #         break
# # # # #
# # # # # for i in range(1,101):
# # # # #     if i%2!=0:
# # # # #         continue
# # # # #
# # # # #     print(i)
# # # #
# # # #
# # # #
# # # # # print("Average calculating fucntion")
# # # #
# # # # # def average (a,*b):
# # # # #     print(a)
# # # # #     print(b)
# # # # #     print(len(b)+1)
# # # # #     for num in b:
# # # # #         a=a+num
# # # # #         d= a/(len(b)+1)
# # # # #     print(d)
# # # # #
# # # # # average(1,2,3,4,5,6)
# # # #
# # # #
# # # #
# # # # # import statistics
# # # # #
# # # # #
# # # # # def a (listt):
# # # # #     print(listt)
# # # # #     cal=statistics.mean(listt)
# # # # #     # result=cal/len(listt)
# # # # #     return cal
# # # # #
# # # # #
# # # # # d=a([1,2,3,4,5])
# # # # # print(d)
# # # #
# # # # # n=(input("Your first number"))
# # # # # m=(input("second number"))
# # # # # try:
# # # # #     print(n*m)
# # # # # except Exception:
# # # # #     print("mistake")
# # # #
# # # # # def detail(name,age=21,address='Teku'):
# # # # #     print(name,age,address)
# # # # #     print(age+5)
# # # # #
# # # # # detail(name='shreejan',age=21)
# # # #
# # # # # print("Calculator")
# # # # #
# # # # # def calculator(nums):
# # # # #
# # # # #     print("Your number:",user)
# # # # #     c=0
# # # # #     for num in nums:
# # # # #         c = c+num
# # # # #     return c
# # # # #
# # # # #
# # # # # user=list(map(int,input("Your number:").split(' ')))
# # # # # result=calculator(user)
# # # # # print(result)
# # # # #
# # # # # a = 10
# # # # # b = 11
# # # # # c = 12
# # # # #
# # # # # def s():
# # # # #
# # # # #     a=99
# # # # #
# # # # #     x=globals()['a']=55
# # # # #
# # # # #     print("inside ", a)
# # # # #
# # # # # s()
# # # # #
# # # # # print("outside", a)
# # # # #
# # # # # print("outside", b)
# # # #
# # # #
# # # # # x=10
# # # # #
# # # # #
# # # # #
# # # # # def a():
# # # # #     global x
# # # # #     x=5
# # # # #     print("Inside",x)
# # # # #
# # # # # a()
# # # # # print("outside",x)
# # # #
# # # # # def f(listt):
# # # # #     print(listt)
# # # # #     odd=0
# # # # #     even=0
# # # # #     for num in listt:
# # # # #         if num%2==0:
# # # # #             even+=1
# # # # #         else:
# # # # #             odd += 1
# # # # #     print(odd,even)
# # # # #
# # # # # f([1,2,3,4,5])
# # # # #
# # # # # def namecal(username):
# # # # #     count=0
# # # # #     for names in username:
# # # # #         if len(names)>5:
# # # # #             print("Name that has more than 5 character:",names)
# # # # #             count+=1
# # # # #         else:
# # # # #             continue
# # # # #     print("There are {} name with more than 5 characters".format(count))
# # # # # user=input("Write 5 names:").split(" ")
# # # # # print("The given names were: ",user)
# # # # # namecal(user)
# # # #
# # # # # c=1
# # # # # def factorial(num):
# # # # #
# # # # #     for i in range(1,num+1):
# # # # #         global c
# # # # #         c=c*i
# # # # #     print(c)
# # # # #
# # # # # number = int(input("Your number:"))
# # # # # factorial(number)
# # # #
# # # # # a= lambda x:x**2
# # # # #
# # # # # result=a(5)
# # # # # print(result)
# # # # # from functools import reduce
# # # # # lis=[2,3,4,5]
# # # # #
# # # # # s = list(map(lambda x:x**2,lis))
# # # # # print(s)
# # # # #
# # # # # f=list(filter(lambda x:x%2==0,lis))
# # # # # print(f)
# # # # #
# # # # # r=reduce(lambda a,b:a+b,lis)
# # # # # print(r)
# # # # # # li2 = []
# # # # # for num in lis:
# # # # #     a=num**2
# # # # #     li2.append(a)
# # # # #
# # # # # print(li2)
# # # #
# # # # # f= lambda a,b,c,d:a+b-c*d
# # # # # r=f(5,5,5,5)
# # # # # print(r)
# # # #
# # # # # import datetime
# # # # #
# # # # # a=datetime.date.today()
# # # # # print(a)
# # # # # b=datetime.time
# # # #
# # # # # print(b)
# # # # name = "shreejan"
# # # # # cast =" Shrestha"
# # # # # a="My name is {} {}".format(name,cast)
# # # # # print(a)
# # # # # print(f'My name is {name} {cast}')
# # # #
# # # #
# # # # def f(normal,*d,**kwargs):
# # # #     print(normal)
# # # #     print(d)
# # # #     for i in d:
# # # #         f=i
# # # #         for n in f:
# # # #             print(n)
# # # #
# # # #
# # # #
# # # # lis=[1,2,3,4,5]
# # # # d={"Name":"Shreejan"}
# # # # f("The name are",lis)
# # #
# # # import Filehandling.Main
# # # import sys
# #
# # # name="Shreejan"
# # # cast ="Shrestha"
# # # age=21
# # # print("The name of my is {} and the cast is {} and my age is {}".format(name,cast,age))
# #
# # # def fact(num):
# # #     a=1
# # #     for numm in range(1,num+1):
# # #         # print(numm)
# # #         a=a*numm
# # #     print(a)
# #
# # #
# # # def fibo(num):
# # #     a=0
# # #     b=1
# # #     # if num ==1:
# # #     #     print(a)
# # #     # elif num==2:
# # #     #     print(a,b)
# # #     for i in range(2,num+1):
# # #         print(a,b,end="")
# # #         c=b+i
# # #         print(c)
# #
# # # a=12344
# # # for i in a:
# # #     print(i)
# #
# # # b="shree"
# # # for i in b:
# # #     print(i)
# # aaa=lambda a:a*a
# # print(aaa)
# # a=[1,2,3]
# # b=[i +5 for i in a ]
# # print(b)
#
# # dict1={i:f"Item {i}" for i in range(3)}
# # print(dict1)
#
# # def set_com(userinput):
# #     s={i for i in userinput}
# #     print("As this is set comprehension the duplicated numbers will only be printed only one time")
# #     print(s)
# #
# # def dict_com(userinput):
# #     d={i:f"Item {i}" for i in userinput}
# #     print(d)
# #
# # def list_com(userinput):
# #     l=[i for i in userinput]
# #     print(l)
# #
# # user=input("What do you want to include in a list").split(" ")
# # print(user)
# # a=list(map(int,user))
# # print("in what format do you want your input want to get represented 1:set_comprihension 2:dic 3:list")
# # usertwo=int(input(":"))
# # if usertwo==1:
# #     set_com(a)
# # elif usertwo==2:
# #     dict_com(a)
# # elif usertwo==3:
# #     list_com(a)
#
#
#
#
# # from functools import reduce
# #
# # a=int(input("Enter the number of items you want\n"))
# # b=int(input("Enter 1 for list, 2 for dict, 3 for set\n"))
# # list1=[i for i in range(a) if b==1]
# # print(list1)
# # dict1={i:f"item{i}" for i in range(a) if b==2}
# # print(dict1)
# #
# # set1={i for i in range(a) if b==3}
# # print(set1)
#
# # l=[1,1,2,3,4]
# # print(len(l))
#
# import os
#
# # print(os.name)
# # print(os.ctermid())
#
# #
# # name='shreejan'
# # print(type(name))
# # for i in name:
# #     print(i)
#
#
# # def allcapatalized(filename):
# #     with open(filename,'r+') as editing:
# #         a=editing.read().split(".")
# #         for sentences in a:
# #             print(sentences.capitalize())
# #
# #
# #
# # user=input("nameplz:")
# #
# # allcapatalized(user)
#
# # s=input("::::")
# # print(type(s))
# # k="shreejan shrestha is my name  "
# # print(k.title())
# # d="shreejan shrestha is my name  "
# # print(d.capitalize())
# # e="shreejan shrestha is my name  "
# # print(e.upper())
# import os
# os.rename('Dictionary.py','dict.py')

# lis=['randy','ortan','john','cina']
# a=" and ".join(lis)
# print(a)
# pic=posterfypdemo.jpg


with open("posterfypdemo.jpg","rb") as b:
    c=b.read()
    with open("newpic.jpg","wb") as a:
        a.write(c)






