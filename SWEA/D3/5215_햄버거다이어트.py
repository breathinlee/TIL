from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    calories = [list(map(int, input().split())) for _ in range(N)]
    max_score = 0
    for k in range(N+1):
        cases = list(combinations([i for i in range(N)], k))
        for case in cases:
            my_sum = 0
            result = 0
            for j in range(len(case)):
                my_sum += calories[case[j]][1]
                result += calories[case[j]][0]
            if my_sum <= L:
                if result > max_score:
                    max_score = result

    print('#{} {}'.format(tc, max_score))