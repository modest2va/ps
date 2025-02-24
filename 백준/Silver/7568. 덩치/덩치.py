a=[]
b=[]
N=int(input())
for i in range(N):
    ki,mugae=map(int,input().split())
    a.append(ki)
    b.append(mugae)
for i in range(N):
    cnt=1
    for j in range(N):
        if a[i]<a[j] and b[i] < b[j]:
            cnt+=1
    print(cnt,end=' ')