from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

arr.sort()

for target in targets:
    index = bisect_left(arr, target)
    if index < len(arr) and arr[index] == target:
        print(1, end=' ')
    else:
        print(0, end=' ')
