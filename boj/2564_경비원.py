N, M = map(int, input().split())   # N: 가로 M: 세로
K = int(input())                   # 상점의 개수
store = [list(map(int, input().split())) for _ in range(K)]     # 방향, 경계로부터의 거리
d_direction, d_distance = map(int, input().split())             # 동근 방향, 경계로부터의 거리
total_distance = 0
# 1은 북쪽, 2는 남쪽, 3은 서쪽, 4는 동쪽
# 왼쪽 경계로부터의 거리 / 위쪽 경계로부터의 거리

for i in range(K):
    if d_direction == store[i][0]:
        total_distance += abs(d_distance - store[i][1])
    if d_direction == 1:    # 북
        if store[i][0] == 2:
            total_distance += min(d_distance + M + store[i][1], N + (N - d_distance) + (M - store[i][1]))
        elif store[i][0] == 3:
            total_distance += d_distance + store[i][1]
        elif store[i][0] == 4:
            total_distance += N - d_distance + store[i][1]
    if d_direction == 2:    # 남
        if store[i][0] == 1:
            total_distance += min(d_distance + M + store[i][1], N + (N - d_distance) + (M - store[i][1]))
        elif store[i][0] == 3:
            total_distance += d_distance + M - store[i][1]
        elif store[i][0] == 4:
            total_distance += N - d_distance + M - store[i][1]
    if d_direction == 3:    # 서
        if store[i][0] == 4:
            total_distance += min(d_distance + N + store[i][1], N + (M - d_distance) + (M - store[i][1]))
        elif store[i][0] == 1:
            total_distance += d_distance + store[i][1]
        elif store[i][0] == 2:
            total_distance += M - d_distance + store[i][1]
    if d_direction == 4:    # 동
        if store[i][0] == 3:
            total_distance += min(d_distance + N + store[i][1], N + (M - d_distance) + (M - store[i][1]))
        elif store[i][0] == 1:
            total_distance += d_distance + N - store[i][1]
        elif store[i][0] == 2:
            total_distance += M - d_distance + N - store[i][1]

print(total_distance)