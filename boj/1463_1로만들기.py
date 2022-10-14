N = int(input())
dp = [0] * (N+1)

for k in range(2, N+1):
    dp[k] = dp[k - 1] + 1

    if k % 2 == 0:
        dp[k] = min(dp[k], dp[k // 2] + 1)

    if k % 3 == 0:
        dp[k] = min(dp[k], dp[k // 3] + 1)

print(dp[N])