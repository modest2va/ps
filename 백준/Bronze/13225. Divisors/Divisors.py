def divisiors(num):
    ans=[]
    for i in range(1,num+1):
        if num%i==0: ans.append(i)
    print(num,len(ans))
for _ in range(int(input())):
    divisiors(int(input()))