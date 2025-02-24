import sys
t=int(sys.stdin.readline())
for _ in range(t):
    j,n=map(int, sys.stdin.readline().split())
    tmp=[]
    for a in range(n):
        r,c=map(int, sys.stdin.readline().split())
        tmp.append(r*c)
    tmp.sort()
    tmp.reverse()
    # print(tmp)
    cnt=1
    tmpCandy=0
    for k in tmp:
        tmpCandy+=k
        # print(tmpCandy)
        if tmpCandy<j :
            cnt+=1
        else:
            print(cnt)
            break
