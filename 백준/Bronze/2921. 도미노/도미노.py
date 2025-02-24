import sys
ans=[]
n=int(sys.stdin.readline())
for i in range(n+1):
    ans.append( (i+1)*3*i/2 )
print( int (sum(ans)))