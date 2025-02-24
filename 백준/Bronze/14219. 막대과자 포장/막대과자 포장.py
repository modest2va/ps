a,b=map(int,input().split())
cnt=0
if a%3!=0 : cnt+=1
if b%3!=0 : cnt+=1
if cnt==2:print("NO")
else: print("YES")