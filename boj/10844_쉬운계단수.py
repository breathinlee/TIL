N = int(input())
dp = [[0] * 10 for _ in range(101)]

for i in range(1, 10):
    dp[1][i] = 1

if N >= 2:
    for k in range(2, N+1):
        for s in range(10):
            if s == 0:
                dp[k][s] = dp[k-1][1]
            elif s == 9:
                dp[k][s] = dp[k-1][8]
            else:
                dp[k][s] = dp[k-1][s-1] + dp[k-1][s+1]

print(sum(dp[N]) % 1000000000)