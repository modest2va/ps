import sys
n=int(sys.stdin.readline())
cnt=0
for i in range(n):
    tmp=list( map( int , (sys.stdin.readline().split())))
    cnt+=sum(tmp)
print(cnt)