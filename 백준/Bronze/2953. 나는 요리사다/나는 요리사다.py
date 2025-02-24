import sys
tmp=[]
for i in range(5):
   tmp.append(sum( map(int, sys.stdin.readline().split())))

checkMax=max(tmp)
for _ in range(5):
    if checkMax==tmp[_]: print("%d %d"%(_+1,checkMax)); break;