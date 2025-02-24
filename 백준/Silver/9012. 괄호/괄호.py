n=int(input())
for i in range(n) :
    s=input()
    for j in range(50) :
        s=s.replace('()','')
    if s=='': print('YES')
    else : print('NO')