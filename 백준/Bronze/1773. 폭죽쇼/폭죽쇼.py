import sys
n,c=map(int, sys.stdin.readline().split())
firework=[0]*(c+1)
for _ in range(n):
    pok=int(sys.stdin.readline())
    for i in range(c+1):
        if i%pok==0: firework[i]=1
print(sum(firework)-1)

