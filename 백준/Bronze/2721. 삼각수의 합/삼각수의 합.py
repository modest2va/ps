import sys
def myt(n):
    return ( ((n+1)*n)//2  )
for i in range(int(sys.stdin.readline())):
    cnt=0
    for j in range(1,int(sys.stdin.readline())+1):
        cnt+=j*myt(j+1)
    print(cnt)