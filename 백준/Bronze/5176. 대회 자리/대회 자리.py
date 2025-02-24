import sys
for _  in range(int(sys.stdin.readline())):
    a,b=map(int,sys.stdin.readline().split())
    tmp=[0]*(b+1)
    cnt=0
    for i in range(a):
        n=int(sys.stdin.readline())
        if tmp[n]==1: cnt+=1
        else: tmp[n]=1
    print(cnt)