from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    distance = [[987654321] * M for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    Q = deque()

    for i in range(N):
        for j in range(M):
            if arr[i][j] == "W":
                distance[i][j] = 0
                Q.append((i, j))

    while Q:
        r, c = Q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == "L" and distance[nr][nc] > distance[r][c] + 1:
                    distance[nr][nc] = distance[r][c] + 1
                    Q.append((nr, nc))

    result = 0
    for i in distance:
        for j in i:
            result += j

    print('#{} {}'.format(tc, result))