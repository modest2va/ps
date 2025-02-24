import sys
n=int(input())
nums=[]
for i in range(n):
    a,b=map(int, sys.stdin.readline().split())
    if a<=b:
        nums.append(b)
if len(nums)==0:
    print(-1)
else :
    print(min(nums))