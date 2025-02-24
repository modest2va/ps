mydp=[0]*101
mydp[1]=1
mydp[2]=1
mydp[3]=1
cnt=int(input())
for _ in range(cnt):
    n=int(input())
    for i in range(4,n+1):

        mydp[i]=(mydp[i-3]+mydp[i-2])
    print(mydp[n])