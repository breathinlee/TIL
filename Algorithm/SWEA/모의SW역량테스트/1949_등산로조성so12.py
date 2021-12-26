def solve(r, c, cnt, construction):
    global ans

    if ans < cnt:
        ans = cnt

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]

        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            if data[r][c] > data[nr][nc]:
                visited[nr][nc] = 1
                solve(nr, nc, cnt + 1, construction)
                visited[nr][nc] = 0
            else:
                if not construction:
                    for j in range(1, K+1):
                        data[nr][nc] -= j
                        if data[r][c] > data[nr][nc]:
                            visited[nr][nc] = 1
                            solve(nr, nc, cnt + 1, True)
                            visited[nr][nc] = 0
                        data[nr][nc] += j


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    ans = 0

    max_height = 0
    for i in range(N):
        for j in range(N):
            if data[i][j] > max_height:
                max_height = data[i][j]

    for i in range(N):
        for j in range(N):
            if data[i][j] == max_height:
                visited = [[0] * N for _ in range(N)]
                visited[i][j] = 1
                solve(i, j, 1, False)

    print('#{} {}'.format(tc, ans))