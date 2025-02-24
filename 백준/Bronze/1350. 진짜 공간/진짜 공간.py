import sys

n=int(sys.stdin.readline())
if n>1:
    tmp=list(map(int, sys.stdin.readline().split()))
    cluster=int(sys.stdin.readline())
    cnt=0
    for i in range(n):
        if tmp[i]!=0:
            if tmp[i]%cluster!=0:
                cnt+=(tmp[i]//cluster) +1
            else: cnt+= tmp[i]//cluster
    print(cnt*cluster)
else:
    tmp=int(sys.stdin.readline())
    cluster=int(sys.stdin.readline())
    if tmp%cluster==0: print(tmp)
    else: print(cluster*(tmp//cluster +1))