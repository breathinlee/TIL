import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    schedule = []
    dp = [0] * (N+1)

    for _ in range(N):
        time, pay = map(int, input().rstrip().split())
        schedule.append((time, pay))

    for k in range(N-1, -1, -1):
        time, pay = schedule[k]

        if k + time > N:
            dp[k] = dp[k+1]

        else:
            dp[k] = max(dp[k+1], dp[k + time] + pay)

    print(dp[0])