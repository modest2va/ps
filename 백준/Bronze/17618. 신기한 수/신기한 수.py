import sys
def singi(n):
    tmp=n
    cnt=0
    while tmp!=0:
        cnt+=tmp%10
        tmp=tmp//10
    if n%cnt==0 : return 1
    else : return 0
n=int(sys.stdin.readline())
ans=0
for i in range(1,n+1):
    if singi(i)==1: ans+=1
print (ans)