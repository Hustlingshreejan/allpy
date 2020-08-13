
user=int(input("Level:"))
# for i in range(user):
#     print('*',end='')
#     for j in range(0,i):
#         print('*',end='')
#     print('')

for i in range(user,0,-1):
    print('*',end='')
    for j in range(i,1,-1):
        print('*',end='')
    print('')