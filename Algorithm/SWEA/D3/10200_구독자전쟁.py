T = int(input())
for tc in range(1, T+1):
    N, A, B = map(int, input().split())
    min_ans = 0  # P채널과 T채널 모두 구독
    max_ans = min(A, B)
    if A + B < N:
        min_ans = 0
    else:
        min_ans = A + B - N

    print('#{} {} {}'.format(tc, max_ans, min_ans))