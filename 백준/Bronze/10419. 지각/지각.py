import sys
for _ in range(int(sys.stdin.readline())):
    n=int(sys.stdin.readline())
    for i in range(10000):
        if i*(i+1)<=n and n< (i+1)*(i+2): print(i); break