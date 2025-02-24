n=int (input())
mydp=[0,1,1]
for i in range(3,n+1):
    mydp.append(mydp[i-1]+mydp[i-2])
print(mydp[n])