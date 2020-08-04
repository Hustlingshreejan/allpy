
def factorial(n):
    c=1
    for i in range(1,n+1):
        c=c*i
    print(c)


user=int(input("Which num's factorial do you want to calculate? :"))
factorial(user)