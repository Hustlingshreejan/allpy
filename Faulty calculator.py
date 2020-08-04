def cal(u):
    '''This calculator can only calculate 2 numbers'''
    if u == 'l':
        first = int(input("Enter your first number: "))
        second = int(input("Enter your second number: "))
        print("Select the operator: ")
        operator = input("* for multiply, / for divide, + for add, - for subtract")
        if first == 45 and second == 3 and operator == '*':
            print("The multiplication of", first, "and", second, "is", 555)
        elif operator == '+':
            print("The addition of", first, "and", second, "is", first + second)
        elif operator == '-':
            print("Substraction is:", first - second)
        elif operator == '*':
            print("Multiplication is:", first * second)
        else:
            print("Division is:", first / second)
        again()
    else:
        print("Multiple operation")
        userformulti=input("Type your operations:")
        result=eval(userformulti)
        print(result)
        again()




def againn():
    u=input("Do you want to calculate 2 or more than 2\n l or m: ")
    return u

def again():

    print("\nDo you want to calculate again??")
    useri=input("Yes:Y No:N \n")
    if useri == 'Y':
        againn()

    else:
        print("Okay")


a=againn()
cal(a)



