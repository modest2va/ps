n,m=map(int, (input().split()))
list_1 = []
for i in range(n):
    list_1.append(list(map(int, input().split())))
k=int(input())
for i in range(k):
    a,b,c,d=map(int,input().split())
    ans=0
    for j in range(a-1,c):
        for k in range(b-1,d):
            ans+=list_1[j][k]
    print(ans)