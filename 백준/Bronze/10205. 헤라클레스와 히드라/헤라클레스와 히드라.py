def sol(n,s):
    for i in s:
        if i=='c':
            n+=1
        elif i=='b':
            n-=1
        if n==0:
            return 0
    return n
k=int(input())
for i in range(k):
    print("Data Set %d:"%(i+1))
    n=int(input())
    s=input()
    print(sol(n,s))
    if i!=k-1:
        print()