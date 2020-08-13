print('Give multiple numbers using space in between')
user = input("Number:").split(' ')
new = list(int(x) for x in user)
print('From new 1', new)
for i in range((len(new))//2):
    new[i], new[-i+-1] = new[-i+-1], new[i]
print(new)