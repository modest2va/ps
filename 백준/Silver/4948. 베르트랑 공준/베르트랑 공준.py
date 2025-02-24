import math
def isPrime(a):
    if a==1 : return False
    n=int(math.sqrt(a))
    for k in range(2,n+1):
        if a%k==0:return False
    return True
mylist=[]
for _ in range (2,246912):
    if isPrime(_) : mylist.append(_)

N=int(input())
while N!=0:
    cnt=0
    for i in mylist:
        if N<i<=N*2:
            cnt+=1
    print(cnt)
    N=int(input())

