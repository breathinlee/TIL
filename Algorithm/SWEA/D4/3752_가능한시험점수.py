T = int(input())
for tc in range(1, T+1):
    N = int(input())
    points = list(map(int, input().split()))
    possible_score = [0]

    for point in points:
        possible_score = list(set(possible_score))
        for i in range(len(possible_score)):
            possible_score.append(possible_score[i] + point)

    ans = len(set(possible_score))
    print('#{} {}'.format(tc, ans))