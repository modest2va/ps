mydp=[0]*1000001
mydp[1]=1
mydp[2]=2
n=int(input())
for i in range(3,n+1):
    mydp[i]=((mydp[i-1]+mydp[i-2])%15746)
print(mydp[n])