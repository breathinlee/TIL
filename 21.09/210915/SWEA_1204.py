T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grades = list(map(int, input().split()))
    cnt = [0] * 101

    for i in range(1000):
        cnt[grades[i]] += 1

    mode = max(cnt)
    cnt.reverse()
    mode_idx = 100 - cnt.index(mode)

    print('#{} {}'.format(tc, mode_idx))