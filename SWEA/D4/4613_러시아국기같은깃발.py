T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())        # N행 M열
    arr = [input() for _ in range(N)]

    white_cnt = [0] * N
    blue_cnt = [0] * N
    red_cnt = [0] * N

    for c in range(N):
        white_cnt[c] = M - arr[c].count('W')
        blue_cnt[c] = M - arr[c].count('B')
        red_cnt[c] = M - arr[c].count('R')

    min_value = N * M

    for w in range(1, N - 1):
        for b in range(w + 1, N):
            cnt = 0
            for i in range(w):
                cnt += white_cnt[i]
            if min_value < cnt:
                break

            for i in range(w, b):
                cnt += blue_cnt[i]
            if min_value < cnt:
                break

            for i in range(b, N):
                cnt += red_cnt[i]

            if min_value > cnt:
                min_value = cnt

    print('#{} {}'.format(tc, min_value))
