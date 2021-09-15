T = int(input())
for tc in range(1, T+1):
    N = int(input())
    position = list(map(int, input().split()))
    distance = []

    for i in range(N):
        ans = abs(position[i])
        distance.append(ans)

        min_distance = min(distance)
        cnt = distance.count(min_distance)

    print('#{} {} {}'.format(tc, min_distance, cnt))