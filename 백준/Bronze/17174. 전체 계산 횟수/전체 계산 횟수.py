import sys
a,b = map(int, sys.stdin.readline().split())
cnt=a
while True:
    cnt+=a//b
    a= a//b
    if a==0: break
print(cnt)