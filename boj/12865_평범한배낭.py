# sol1

import sys

N, K = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if j < arr[i-1][0]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-arr[i-1][0]] + arr[i-1][1])

print(dp[-1][-1])


# sol2(sol1 압축)
import sys

N, K = map(int, sys.stdin.readline().split())
dp = [0] * (K + 1)
for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())
    for i in range(K, W-1, -1):
        dp[i] = max(dp[i], dp[i-W] + V)
print(dp[K])