import sys
input = sys.stdin.readline

N = int(input())
schedule = []
dp = [0] * (N+1)

for _ in range(N):
    time, pay = map(int, input().rstrip().split())
    schedule.append((time, pay))

for k in range(N-1, -1, -1):
    if k + schedule[k][0] > N:
        dp[k] = dp[k+1]

    else:
        dp[k] = max(dp[k + schedule[k][0]] + schedule[k][1], dp[k+1])

print(dp[0])