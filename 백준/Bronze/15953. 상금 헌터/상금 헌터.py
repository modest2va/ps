import sys
for _ in range(int(sys.stdin.readline())):
    cnt=0
    a,b=map(int, sys.stdin.readline().split())
    if a==1: cnt+=5000000
    elif a>=2 and a<=3: cnt+=3000000
    elif a >= 4 and a <= 6: cnt += 2000000
    elif a >= 7 and a <= 10: cnt += 500000
    elif a >= 11 and a <= 15: cnt += 300000
    elif a >= 16 and a <= 21: cnt += 100000

    if b==1: cnt+=5120000
    elif b>=2 and b<=3: cnt+=2560000
    elif b >= 4 and b <= 7: cnt += 1280000
    elif b >= 8 and b <= 15: cnt += 640000
    elif b >= 16 and b <= 31: cnt += 320000
    print(cnt)