# sol 1 - 11로 제한

T = int(input())
for _ in range(T):
    n = int(input())
    dp = [0] * 11
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for k in range(4, 11):
        dp[k] = dp[k-1] + dp[k-2] + dp[k-3]

    print(dp[n])


# sol 2 - 일반화 (22-28번째 줄처럼 조건분기 안해주면 n이 4보다 작을경우 33번째 줄에서 인덱스에러남)
T = int(input())
for _ in range(T):
    n = int(input())
    dp = [0] * (n+1)
    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    elif n == 3:
        print(4)
    else:
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4

        for k in range(4, n+1):
            dp[k] = dp[k-1] + dp[k-2] + dp[k-3]

        print(dp[n])