# 0: 현재 속도 유지, 1: 가속, 2: 감속

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    velocity = 0
    distance = 0

    for i in range(N):
        if arr[i][0] == 1:
            velocity += arr[i][1]
        elif arr[i][0] == 2:
            if velocity < arr[i][1]:
                velocity = 0
            else:
                velocity -= arr[i][1]
        distance += velocity

    print('#{} {}'.format(tc, distance))
