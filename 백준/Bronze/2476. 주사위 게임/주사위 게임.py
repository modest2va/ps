import sys
n=int(sys.stdin.readline())
tmp=[]
for _ in range(n):
    a,b,c=map(int,sys.stdin.readline().split())
    if a==b==c: tmp.append(10000+a*1000)
    elif a==b or a==c : tmp.append(1000+100*a)
    elif b==c: tmp.append(b*100+1000)
    else : tmp.append(max(a,b,c)*100)
print(max(tmp))