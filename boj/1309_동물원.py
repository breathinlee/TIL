# 가로 2 세로 N 
# 사자들은 가로로 혹은 세로로 붙어 있게 배치 불가능
# input 4 => output 41

import sys

input = sys.stdin.readline

N = int(input())

dp = [[0] * 3 for _ in range(N+1)]

dp[1][0] = dp[1][1] = dp[1][2] = 1

for i in range(2, N+1):
    dp[i][0] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2]
    dp[i][0] %= 9901
    dp[i][1] = dp[i-1][0] + dp[i-1][2]
    dp[i][1] %= 9901
    dp[i][2] = dp[i-1][0] + dp[i-1][1]
    dp[i][2] %= 9901

answer = sum(dp[N]) % 9901
print(answer)