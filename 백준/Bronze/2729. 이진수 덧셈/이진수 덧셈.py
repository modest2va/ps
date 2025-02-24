def deciTobin(a):
    lenA=len(a)
    numA=0
    for i in range(lenA):
        numA+=int(a[i])*pow(2,lenA-i-1)
    return numA
n=int(input())
for _ in range(n):
    ans=[0]*81
    a,b=input().split()
    print(bin(deciTobin(a)+deciTobin(b) )[2:])
