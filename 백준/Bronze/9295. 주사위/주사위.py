import sys
for i in range(1,int(sys.stdin.readline())+1):
    tmp=list(map(int,sys.stdin.readline().split()))
    print ("Case %d: %d"%(i,sum(tmp)))