print("Welcome to pattern printing")
for i in range(0,5):
    print('*', end=" ")
    for j in range(1,i+1):
        print('#',end=" ")

    print()

print('#')
for i in range(5,0,-1):
    for j in range(i,1,-1):
        print('#', end=' ')
    print('#',end=" ")

    print()

print('*')
print('*')