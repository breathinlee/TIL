def find_best_hamburger(idx, sum_score, sum_calorie):
    global ans

    if sum_calorie > L:
        return

    if idx >= N:
        if ans < sum_score:
            ans = sum_score
        return

    find_best_hamburger(idx+1, sum_score + scores[idx], sum_calorie + calories[idx])
    find_best_hamburger(idx+1, sum_score, sum_calorie)


T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    scores = []
    calories = []
    ans = 0

    for _ in range(N):
        score, calorie = map(int, input().split())
        scores.append(score)
        calories.append(calorie)

    find_best_hamburger(0, 0, 0)

    print('#{} {}'.format(tc, ans))