def calculate_binomial_coefficient(n, k):
    if k < 0 or k > n:
        return 0
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    return dp[n][k]

# 입력 받기
n, k = map(int, input().split())

# n번째 행의 k번째 수 출력
result = calculate_binomial_coefficient(n - 1, k - 1)
print(result)
