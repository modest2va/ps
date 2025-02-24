import sys
import math
def checkPrime(n):
    sieve=[True]*n
    a=int(math.sqrt(n))
    for i in range(2,a+1):
        if sieve[i]:
            for j in range(i+i,n,i):
                sieve[j]=False
    return [i for i in range(2,n) if sieve[i]==True]

p,k=map(int, sys.stdin.readline().split())
ans=0
tmp=checkPrime(k)
for i in range (len(tmp)):
    if p%tmp[i]==0:
        print("BAD %d"%tmp[i])
        exit()
if ans==0: print("GOOD")