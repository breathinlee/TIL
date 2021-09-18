T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    ans = -1

    if A >= 10 or B >= 10:
        pass
    else:
        ans = A * B

    print('#{} {}'.format(tc, ans))