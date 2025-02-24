cnt=1
while 1:
    l,p,v=map(int,input().split())
    if l==0 and p==0 and v==0 : break
    else:
        ans= (v//p)*l + min(v%p,l)
        print("Case %d: %d"%(cnt,ans))
        cnt+=1