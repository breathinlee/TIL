from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]
    sum_synergy = [[0] * N for _ in range(N)]
    result = 987654321

    for i in range(N):
        for j in range(N):
            sum_synergy[i][j] = synergy[i][j] + synergy[j][i]

    cases = list(combinations([i for i in range(N)], N//2))
    for case in cases:
        A, B = 0, 0
        numbers = list(range(N))
        for k in case:
            numbers.remove(k)
        A_cases = list(combinations(case, 2))
        B_cases = list(combinations(numbers, 2))

        for a_case in A_cases:
            A += sum_synergy[a_case[0]][a_case[1]]
        for b_case in B_cases:
            B += sum_synergy[b_case[0]][b_case[1]]

        difference = abs(A - B)

        if difference < result:
            result = difference

    print('#{} {}'.format(tc, result))