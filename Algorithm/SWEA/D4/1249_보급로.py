def find_route(r, c):
    queue = [(r, c)]

    while queue:
        x, y = queue.pop(0)

        for k in range(4):
            nx = x + dr[k]
            ny = y + dc[k]

            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] + time[x][y] < time[nx][ny]:
                    time[nx][ny] = arr[nx][ny] + time[x][y]
                    queue.append((nx, ny))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    time = [[987654321] * N for _ in range(N)]
    time[0][0] = 0
    result = 0

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    find_route(0, 0)

    print('#{} {}'.format(tc, time[N-1][N-1]))