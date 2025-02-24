a,b,c=map(int, input().split())
ans=b-a
if ans%c ==0: print(ans//c)
else: print(ans//c +1)