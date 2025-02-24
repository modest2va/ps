operation='('+str(input())
while 1:
    s=input()
    if s=='=':
        break
    operation += s
    if s.isnumeric():
        operation+=')'
if operation.count('(')<operation.count(')'):
    operation='('*(operation.count(')')-operation.count('('))+operation
operation=operation.replace('/','//')
print(eval(operation))