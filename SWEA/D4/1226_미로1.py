def check(start):
    queue = [start]
    visited[start[0]][start[1]] = 1

    while queue:
        r, c = queue.pop(0)

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < 16 and 0 <= nc < 16 and not visited[nr][nc] and maze[nr][nc] != 1:
                if maze[nr][nc] == 3:
                    return 1
                visited[nr][nc] = 1
                queue.append((nr, nc))

    return 0


for _ in range(1, 11):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start = (i, j)
                break

    ans = check(start)
    print('#{} {}'.format(tc, ans))