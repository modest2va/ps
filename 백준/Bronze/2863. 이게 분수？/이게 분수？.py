import sys
a,b=map(int,sys.stdin.readline().split())
c,d=map(int,sys.stdin.readline().split())
tmp=[]
tmp.append(a/c+b/d)
tmp.append(c/d+a/b)
tmp.append(d/b+c/a)
tmp.append(b/a+d/c)

for i in range(4):
    if tmp[i]==max(tmp): print(i); break
