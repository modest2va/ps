def bubble_sort(arr, k):
    answer = [-1]
    cnt = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                cnt += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
                if cnt == k:
                    return arr[j], arr[j + 1]
    return answer

n, k = map(int, input().split())
arr = list(map(int, input().split()))

print(*bubble_sort(arr, k))

