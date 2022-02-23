directions = [(-1, 1), (1, 1), (1, -1), (-1, -1)]

def dfs(r, c, d, start, dessert):
    global result

    if d > 3:
        return

    nr = r + directions[d][0]
    nc = c + directions[d][1]

    # if (nr < 0 and nc < 0) or (nr < 0 and nc >= N) or (nr >= N and nc < 0) or (nr >= N and nc >= N):
    #     return

    if (nr, nc) == start and d == 3:
        if result < len(dessert):
            result = len(dessert)
        return

    if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] not in dessert:
        dfs(nr, nc, d, start, dessert + [arr[nr][nc]])
        dfs(nr, nc, d+1, start, dessert + [arr[nr][nc]])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = -1

    for i in range(N):
        for j in range(N):
            dessert = [arr[i][j]]
            start_point = (i, j)
            dfs(i, j, 0, start_point, dessert)

    print('#{} {}'.format(tc, result))