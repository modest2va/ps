n=int(input())

mydp=[]

mydp.append(0)
mydp.append(0)
mydp.append(1)
mydp.append(1)
for i in range(4,n+1):
    mydp.append(mydp[i-1]+1);
    if(i%2==0):
        mydp[i]=min(mydp[i],mydp[i//2]+1)
    if(i%3==0):
        mydp[i]=min(mydp[i],mydp[i//3]+1)
print(mydp[n])