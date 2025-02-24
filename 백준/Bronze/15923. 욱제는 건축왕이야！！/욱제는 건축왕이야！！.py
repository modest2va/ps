import sys
n=int(sys.stdin.readline())
tmp=[]
for  i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    tmp.append( (a,b) )
cnt=0
for i in range(1,n):
    cnt+= abs (tmp[i][0]-tmp[i-1][0]) + abs (tmp[i][1]-tmp[i-1][1])
print(cnt + abs (tmp[0][0]-tmp[len(tmp)-1][0]) + abs (tmp[0][1]-tmp[len(tmp)-1][1]))