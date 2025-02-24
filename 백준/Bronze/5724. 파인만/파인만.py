import sys
def pinman(n):
    cnt=0
    for i in range(1,n+1):
        cnt+=pow(i,2)
    return(cnt)
while True:
    n=int(sys.stdin.readline())
    if n==0: exit()
    else: print(pinman(n))