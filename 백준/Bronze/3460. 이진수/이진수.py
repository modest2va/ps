import sys
t=int(sys.stdin.readline())
for _ in  range(t):
    n=int(sys.stdin.readline())
    tmp=[]
    while n//2!=0:
        tmp.append(n%2)
        n=n//2
    tmp.append(n%2)
    #print (tmp)
    for i in range(len(tmp)):
        if tmp[i]==1: s=print(i,end=' ')
   