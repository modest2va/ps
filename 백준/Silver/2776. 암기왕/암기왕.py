import bisect
t = int(input())
for i in range(t):
    n = int(input())
    diary1 = list(map(int, input().split()))
    m = int(input())
    diary2 = list(map(int, input().split()))

    diary1.sort()
    for target in diary2:
        index = bisect.bisect_left(diary1, target)
        if index < n and diary1[index] == target:
            print(1)
        else:
            print(0)
    #####