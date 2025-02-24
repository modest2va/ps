import sys
n,a,b=map(int, sys.stdin.readline().split())
tmp=[ list (map(int,sys.stdin.readline().split())) for _ in range (n) ]
cnt=0
jinseo=tmp[a-1][b-1]
for _ in range(n):
    if jinseo<tmp[_][b-1]: print("ANGRY"); cnt=1; exit()

for _ in range(n):
    if jinseo < tmp[a-1][_]: print("ANGRY"); cnt=1; exit()

if cnt==0: print("HAPPY")