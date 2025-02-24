from collections import deque
import sys
ans=deque()
n=int(input())
for i in range(n):
    tmp=list(sys.stdin.readline().split())
    if tmp[0]=='push' : ans.append(int(tmp[1]))
    if tmp[0]=='front' :
        if len(ans)==0: print(-1)
        else: print(ans[0])
    if tmp[0]=='back' :
        if len(ans)==0: print(-1)
        else: print(ans[-1])
    if tmp[0]=='size': print(len(ans))
    if tmp[0]=='empty':
        if len(ans)==0 : print(1)
        else :print (0)
    if tmp[0]=='pop':
        if len(ans)==0: print (-1)
        else:
            print(ans[0])
            ans.popleft()