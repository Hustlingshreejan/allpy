


def cal_palindrome(num):
    num = num+1
    while not is_palindrome(num):
        num += 1
    return num

def is_palindrome(num):
    return str(num) == str(num)[::-1]


if __name__ == '__main__':
    try:
        user1 = int(input("Number of input?\n->"))
        # first empty list to store user's input
        first_list = []
        for i in range(user1):
            try:
                user2 = int(input("Your number?\n->"))
                first_list.append(user2)
            except Exception as e:
                print("The input must be integer")
                exit()
        print("The numbers you provided to the system to check the palindrome:", first_list,'\nThe value less than 10 is palindrome by itself.')
        # second empty list to store the final result after calculating palindrome
        second_list = []
        for nums in first_list:
            if nums < 10:
                second_list.append(nums)
            else:
                val = cal_palindrome(nums)
                second_list.append(val)
        print(second_list)
    except Exception as e:
        print('The value must be integer')
        exit()
