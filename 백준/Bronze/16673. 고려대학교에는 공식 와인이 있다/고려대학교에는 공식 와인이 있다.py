import sys
c,k,p=map( int , (sys.stdin.readline().split()))
cnt=0
for i in range(c+1):
    cnt+=i*(i*p+k)
print(cnt)