from bisect import bisect_left

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    targets = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    arr.sort()

    answer = 0
    for target in targets:
        index = bisect_left(arr, target)
        answer += index
    print(answer)

