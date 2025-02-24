n=int(input())
m=int(input())
ingredientList=list(map(int, input().split()))
ingredientList.sort()
start,end=0,n-1
ans=0
while start < end:
   target=ingredientList[start]+ingredientList[end]
   if  target==m:
      ans+=1
      end-=1
      start+=1
   elif target>m: end-=1
   else : start+=1
print(ans)