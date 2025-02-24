import sys
n=int(sys.stdin.readline())
ox=list(map(int, sys.stdin.readline().split()))
if ox[0]==0: ans=0;cnt=0
else: ans=1; cnt=1
for i in range(1,n):
    if ox[i-1]==1:
        if ox[i]==1:
            cnt+=1; ans+=cnt
        else: cnt=0
    else :
        if ox[i]==1: cnt+=1;ans+=1
        else: cnt=0
print(ans)
