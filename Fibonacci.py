def fibo(num):
    a = 0
    b = 1
    if num == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(3,num+1):
            c=a+b
            a=b
            b=c
            print(c)

def askuser():
    user=int(input("How many numbers? "))
    if user < 1:
        print("Invalid input\n")
        print("Want to try again?\n ")
        usersecond=input("Y for yes N for No:")
        if usersecond == 'Y':
            askuser()
    else:
        fibo(user)

askuser()

