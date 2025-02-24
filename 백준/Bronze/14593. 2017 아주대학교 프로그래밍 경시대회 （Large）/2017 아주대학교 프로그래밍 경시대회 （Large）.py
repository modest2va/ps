cnta=0
cntb=999
cntc=999
ans=0
for i in range(int (input())):
    a,b,c=map(int,input().split())
    if cnta<a: cnta=a; cntb=b;cntc=c;ans=i+1
    if cnta==a:
        if cntb>b: cnta=a; cntb=b;cntc=c;ans=i+1
        if cntb==b:
           if cntc>c: cnta=a; cntb=b;cntc=c;ans=i+1
print(ans)