tmp=[]
for i in range(int(input())):
    a,b=map(str, input().split())
    if b=='enter' :
        tmp.append(a)
    elif b=='leave':
        tmp.remove(a)

for i in sorted(tmp,reverse=True):
    print (i)