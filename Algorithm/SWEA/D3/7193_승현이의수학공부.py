T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())
    X = str(X)
    decimal_X = 0
    if N == 2:
        ans = 0
    else:
        for i in range(len(X)):
            decimal_X += int(X[-1-i]) * (N ** i)
        ans = decimal_X % (N-1)

    print('#{} {}'.format(tc, ans))