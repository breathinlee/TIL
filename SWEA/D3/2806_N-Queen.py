def check(k):
    global cnt

    if k == N:
        cnt += 1
        return

    for i in range(N):
        if row[i] or n_diagonal[i + k] or p_diagonal[i - k]:
            continue
        row[i] = n_diagonal[i + k] = p_diagonal[i - k] = 1
        check(k+1)
        row[i] = n_diagonal[i + k] = p_diagonal[i - k] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    row = [0] * N
    p_diagonal = [0] * (2 * N - 1)
    n_diagonal = [0] * (2 * N - 1)
    cnt = 0

    check(0)
    print('#{} {}'.format(tc, cnt))