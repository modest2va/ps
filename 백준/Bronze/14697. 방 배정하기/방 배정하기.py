a,b,c,n=(map(int,input().split()))
cnt=0
for i in range(51):
    for j in range(51):
        for k in range(51):
            if a*i + b*j +c*k ==n: cnt=1; break
print(cnt)