import sys
while  1:
    tmp=list(map(int, sys.stdin.readline().split()))
    if tmp[0]==0: exit()
    else:
        ans=1
        if tmp[0]==1: print(tmp[1]-tmp[2])
        else:
            for i in range(1,tmp[0]+1):
                ans=tmp[i*2-1]*ans-tmp[i*2]
            print(ans)