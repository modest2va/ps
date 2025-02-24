import sys
cnt=0
for _ in range (int(sys.stdin.readline())):
    a,b=map(int,sys.stdin.readline().split())
    cnt+=b%a
print(cnt)