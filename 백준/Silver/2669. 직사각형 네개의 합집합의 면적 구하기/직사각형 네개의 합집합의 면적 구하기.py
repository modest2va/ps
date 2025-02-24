arr= [[0 for col in range(101)] for row in range(101)]
for i in range(4):
    a,b,c,d=map(int,input().split())
    for j in range(a,c):
        for k in range(b,d):
            arr[j][k]=1
mysum=0
for i in range(101):
    mysum+=sum(arr[:][i])
print(mysum)