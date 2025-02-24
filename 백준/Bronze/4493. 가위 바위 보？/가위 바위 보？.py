import sys
n=int(sys.stdin.readline())
for _ in range(n):
    a=int(sys.stdin.readline())
    cnt1=0
    cnt2=0
    for i in range(a):
        p1,p2=sys.stdin.readline().split()
        if p1=='R':
            if p2=='P':cnt2+=1
            elif p2=='S':cnt1+=1
        if p1 == 'P':
            if p2 == 'R':
                cnt1 += 1
            elif p2 == 'S':
                cnt2 += 1
        if p1=='S':
            if p2=='P':cnt1+=1
            elif p2=='R':cnt2+=1
    if cnt1>cnt2: print("Player 1")
    elif cnt1 < cnt2: print("Player 2")
    elif cnt1 == cnt2: print("TIE")
