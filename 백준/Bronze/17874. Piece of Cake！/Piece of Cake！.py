n,h,v=map(int,input().split())
ans=max(h*v,h*(n-v),(n-h)*v,(n-h)*(n-v))
print(4*ans)