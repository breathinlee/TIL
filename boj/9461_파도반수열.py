dp = [0] * 101
dp[0] = dp[1] = dp[2] = 1

T = int(input())
for _ in range(T):
    N = int(input())

    if N <= 2:
        print(dp[N])
    else:
        for k in range(3, N+1):
            dp[k] = dp[k-3] + dp[k-2]
        print(dp[N-1])