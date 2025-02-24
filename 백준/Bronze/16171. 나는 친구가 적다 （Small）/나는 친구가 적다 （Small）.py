s1 = input()
s2 = input()
number = '0123456789'
for i in number:
    s1 = s1.replace(i, '')
if s2 in s1:
    print(1)
else:
    print(0)