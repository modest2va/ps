import bisect

# 입력
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

# 배열을 정렬
arr.sort()
#arr = sorted(arr)

# 이진 탐색을 사용하여 각 수가 존재하는지 확인하고 결과 출력
for target in targets:
    index = bisect.bisect_left(arr, target)
    if index < len(arr) and arr[index] == target:
        result = 1
    else:
        result = 0
    print(result)