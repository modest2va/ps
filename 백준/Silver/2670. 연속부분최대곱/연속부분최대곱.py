n=int(input())
realNumbers=[float(input()) for i in range(n)]
dp=[realNumbers[0]]
for i in range(n-1):
    dp.append(max(dp[i]*realNumbers[i+1],realNumbers[i+1]))
print("%.3f"%(max(dp)))