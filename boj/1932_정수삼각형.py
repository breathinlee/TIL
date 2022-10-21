import sys
input = sys.stdin.readline

n = int(input())
dp = []
for _ in range(n):
    tmp = list(map(int, input().rstrip().split()))
    dp.append(tmp)

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][0] += dp[i-1][0]
        elif j == i:
            dp[i][i] += dp[i-1][i-1]
        elif 0 < j < i:
            dp[i][j] = max(dp[i-1][j-1] + dp[i][j], dp[i-1][j] + dp[i][j])

print(max(dp[n-1]))