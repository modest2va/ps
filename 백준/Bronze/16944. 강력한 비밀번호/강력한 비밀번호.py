n = int(input())
s = input()

conditions = [1,1,1,1]
special = '!@#$%^&*()-+'
for i in s:
    if i.isdigit():
        conditions[0] = 0
    if i.islower():
        conditions[1] = 0
    if i.isupper():
        conditions[2] = 0
    if i in special:
        conditions[3] = 0
n += sum(conditions)
if  n > 6 :
    print(sum(conditions))
else:
    print(6 - n + sum(conditions))