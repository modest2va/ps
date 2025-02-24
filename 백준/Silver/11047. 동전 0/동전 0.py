a=list(map(int, input().split()))
moneyList=[]
for _ in range (a[0]):
    moneyList.append(int(input()))
moneyList.sort(reverse=True)
cnt=0
for _ in range(a[0]):
    cnt+=int (a[1]/moneyList[_])
    a[1]=int(a[1]%moneyList[_])
print(cnt)
