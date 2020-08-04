print("Check prime number")
user=int(input("Type your number: "))
for i in range(2,user):
    if user%i==0:
        print("This number is not prime")
        break
else:
    print("This number is prime")