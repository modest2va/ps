a,b,c,d=map(int,input().split())
tmp1=[c]
tmp2=[d]
ans=-1
for _ in range(1000):
    c+=a;d+=b
    tmp1.append(c);tmp2.append(d)
    if c in tmp2 or d in tmp1: ans=min(c,d); break
print(ans)