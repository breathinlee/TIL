import sys
input = sys.stdin.readline

N = int(input())
passengers = [0] + list(map(int, input().split()))
M = int(input())

dp = [[0] * (N + 1) for _ in range(4)]

for i in range(4):
    for j in range(1, N+1):
        if i == 0:
            dp[i][j] = dp[i][j-1] + passengers[j]
        elif j < i*M:
            continue
        elif i == 1 and j >= i*M:
            dp[i][j] = max(dp[i][j-1], dp[0][j]-dp[0][j-M])
        else:
            dp[i][j] = max(dp[i][j-1], (dp[i-1][j-M] + dp[0][j] - dp[0][j-M]))


print(dp[3][N])