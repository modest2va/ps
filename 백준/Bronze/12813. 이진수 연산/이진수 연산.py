a=input()
b=input()
for i in range(len(a)):
    if a[i]== '1' and b[i]=='1' : print('1',end='')
    else: print('0',end='')
print()
for i in range(len(a)):
    if a[i]== '1' or b[i]=='1' : print('1',end='')
    else: print('0',end='')
print()
for i in range(len(a)):
    if int(a[i])+int(b[i])==1 : print('1',end='')
    else: print('0',end='')
print()
for i in range(len(a)):
    if a[i]=='1' : print('0',end='')
    else: print('1',end='')
print()
for i in range(len(a)):
    if b[i]=='1' : print('0',end='')
    else: print('1',end='')