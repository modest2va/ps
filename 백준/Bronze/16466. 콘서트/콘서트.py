import sys
n=int(sys.stdin.readline())
nums=sorted(list(map(int, sys.stdin.readline().split())))
is_full=1
for i in range(len(nums)):
    if (i+1)!=nums[i]:
        print(i+1)
        is_full=0
        break
if is_full == 1:
    print(n+1)