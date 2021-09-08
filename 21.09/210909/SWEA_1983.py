# sol 1
grade_list = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    grades = [list(map(int, input().split())) for _ in range(N)]
    score_list = []
    for grade in grades:
        total = (grade[0] * 0.35) + (grade[1] * 0.45) + (grade[2] * 0.2)
        score_list.append(total)

    K_score = score_list[K-1]
    score_list.sort(reverse=True)
    tmp = N // 10
    matching_K_grade = score_list.index(K_score) // tmp

    print('#{} {}'.format(tc, grade_list[matching_K_grade]))


# so1 2
grade_list = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    grades = [list(map(int, input().split())) for _ in range(N)]
    score_list = []
    for grade in grades:
        total = (grade[0] * 0.35) + (grade[1] * 0.45) + (grade[2] * 0.2)
        score_list.append(total)

    result = [(score, idx) for idx, score in enumerate(score_list)]
    result.sort(reverse=True)

    tmp = N // 10
    K_grade = 0

    for i in range(N):
        if result[i][1] == K-1:
            K_grade = i // tmp

    print('#{} {}'.format(tc, grade_list[K_grade]))
