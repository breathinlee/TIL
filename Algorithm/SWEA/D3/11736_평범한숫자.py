T = int(input())
for tc in range(1, T+1):
    N = int(input())
    sequence = list(map(int, input().split()))
    cnt = 0

    for i in range(1, N-1):
        if max(sequence[i-1], sequence[i], sequence[i+1]) != sequence[i] and min(sequence[i-1], sequence[i], sequence[i+1]) != sequence[i]:
            cnt += 1

    print('#{} {}'.format(tc, cnt))