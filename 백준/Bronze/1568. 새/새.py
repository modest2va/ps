import sys

n=int(sys.stdin.readline())
tmp=0
for _ in range(99999):
    if n <= 0: break
    else :
        cnt = 1
        while n>0:
            if n-cnt<0 : break
            n-=cnt
            cnt+=1
            tmp+=1

print(tmp)
