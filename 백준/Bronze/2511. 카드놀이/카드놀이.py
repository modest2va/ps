import sys
a=list(map(int, sys.stdin.readline().split()))
b=list(map(int, sys.stdin.readline().split()))
ansa=0
ansb=0

acnt=0
bcnt=0

for i in range(10):
    if a[i]>b[i]:ansa+=3; acnt=i
    if a[i] < b[i]: ansb += 3; bcnt=i
    if a[i] == b[i]: ansa += 1; ansb+=1

if ansa>ansb: print("%d %d"%(ansa,ansb));print("A")
if ansa<ansb: print("%d %d"%(ansa,ansb));print("B")
if ansa==ansb:
    if ansa==ansb and ansa==10:
        print("10 10")
        print("D")
    else:
        if acnt > bcnt: print("%d %d"%(ansa,ansb));print("A")
        if acnt < bcnt: print("%d %d"%(ansa,ansb));print("B")

