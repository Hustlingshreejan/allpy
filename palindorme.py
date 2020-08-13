# user=int(input("How many times you want to give a input"))
#
# for times in range(user):
#     usertwo=input("Give:")
#     if usertwo[0]==usertwo[-1]:
#         print("It itself is the palen")
#     else:
#         while(True):
#             usertwo+=1
#             if usertwo[0] == usertwo[-1]:
#                 print("The next  palen is",usertwo)
#                 break


# user=input("Provide the input:")
# print(user)
# l=[]
# for i in range(len(user)):
#     l.append(user[i])
# a=l[:]
# a.reverse()
# if l ==a:
#     print("it")
# else:
#     new=list(int(i) for i in l)
#     print(new)
#
'''
Author: Harry
Date: 15 April 2019
Purpose: Practice Problem For CodeWithHarry Channel 
'''


def next_palindrome(n):
    b = n+1
    while not is_palindrome(b):
        b += 1
    return b

def is_palindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == "__main__":
    try:
        n = int(input("Enter the number of test cases\n"))
        numbers = []
        for i in range(n):
            try:
                number = int(input("Enter the number:\n"))
                numbers.append(number)

            except Exception as e:
                print("It must be number")
                exit()

        for i in range(n):
            print(
                f"Next palindrome for {numbers[i]} is {next_palindrome(numbers[i])}")
    except Exception as e:
        print("The value must be integer")
        exit()


