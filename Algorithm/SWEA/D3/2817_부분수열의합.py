from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())       # N개의 자연수, 그 합 K
    A = list(map(int, input().split()))
    cnt = 0

    # K 초과하는 값들 제거
    for tmp in A:
        if tmp > K:
            while tmp in A:
                A.remove(tmp)
    # 리스트 내 K와 같은 값 있으면 count
    for tmp in A:
        if tmp == K:
            cnt += 1

    # 몇 개의 원소의 합이 K가 되는 경우
    for j in range(2, len(A)+1):
        cases = list(combinations([i for i in range(0, len(A))], j))
        for case in cases:
            my_sum = 0
            for k in range(j):
                my_sum += A[case[k]]
            if my_sum == K:
                cnt += 1

    print('#{} {}'.format(tc, cnt))
