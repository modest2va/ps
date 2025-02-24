import sys
a,b=map(int, sys.stdin.readline().split())
n=int(sys.stdin.readline())
tmp=[]
for i in range(n):
    tmp.append(abs(b- int(sys.stdin.readline())))
heu=min(tmp)
if abs(a-b)>heu: print(heu+1)
else : print(abs(a-b))
