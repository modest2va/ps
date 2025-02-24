import sys
for _ in range (int(sys.stdin.readline())):
    change=int(sys.stdin.readline())
    a=change//25; change%=25
    b=change//10; change%=10
    c=change//5; d=change%5
    print("%d %d %d %d"%(a,b,c,d))