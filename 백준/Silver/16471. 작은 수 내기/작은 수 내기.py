import sys
n=int(sys.stdin.readline())
tmp1=sorted(list(map(int, sys.stdin.readline().split())))
tmp2=sorted(list(map(int, sys.stdin.readline().split())))
tmp1.reverse()
cnt=0
for i in tmp1:
  if i>=tmp2[-1]:
    pass
  else:
    cnt+=1
    tmp2.pop()
if cnt> n//2: print("YES")
else: print("NO")