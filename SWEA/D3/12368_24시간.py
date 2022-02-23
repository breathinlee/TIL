T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())

    time = A + B
    if time > 24:
        time %= 24
    elif time == 24:
        time = 0

    print('#{} {}'.format(tc, time))