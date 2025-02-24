def sol(s):
    pikachu = ['pi', 'ka', 'chu']
    for i in pikachu:
        s = s.replace(i, '*'*len(i))
    if len(s)==s.count('*'):
        return True
    else:
        return False
s=input()
if sol(s) == True:
    print("YES")
else:
    print("NO")