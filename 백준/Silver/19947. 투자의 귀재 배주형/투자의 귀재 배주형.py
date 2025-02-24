def sol(money, years):
    a_type, b_type, c_type = 1.05, 1.20, 1.35
    dp = [0] * (years + 1)
    dp[0] = money
    for i in range(1, years + 1):
        if i >= 5:
            dp[i] = int(max(dp[i - 1] * a_type, dp[i - 3] * b_type, dp[i - 5] * c_type))
        elif i >= 3:
            dp[i] = int(max(dp[i - 1] * a_type, dp[i - 3] * b_type))
        else:
            dp[i] = int(dp[i - 1] * a_type)
    return dp[years]


if __name__ == '__main__':
    money, years = map(int, input().split())
    print(sol(money, years))
