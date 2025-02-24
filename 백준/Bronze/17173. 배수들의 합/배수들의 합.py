n,m=map(int,input().split())
ki=list(map(int,input().split()))
tmp=[]
for i in ki:
    for j in range(i,n+1):
        if j%i ==0:tmp.append(j)
print(sum(set(tmp)))