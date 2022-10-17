N = int(input())
stairs = [int(input()) for _ in range(N)]
dp = [0] * 301

if N == 1:
    print(stairs[0])
elif N == 2:
    print(stairs[0] + stairs[1])
else:
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

    for k in range(3, N):
        dp[k] = max(dp[k-2] + stairs[k], dp[k-3] + stairs[k-1] + stairs[k])

    print(dp[N-1])