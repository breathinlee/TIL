def find_route(r, c, d, start_point, cnt):
    global max_cnt

    if d > 3:
        return

    for k in range(2):
        nr = r + direction[d][0]
        nc = c + direction[d][1]
        if 0 <= nr < N and 0 <= nc < N:
            if d == 3 and (nr, nc) == start_point:
                if max_cnt < cnt:
                    max_cnt = cnt
                    return
            elif cafe[nr][nc] not in dessert:
                dessert.append(cafe[nr][nc])
                find_route(nr, nc, d+k, start_point, cnt+1)
                dessert.remove(cafe[nr][nc])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    direction = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    max_cnt = -1

    for i in range(N):
        for j in range(N):
            dessert = [cafe[i][j]]
            find_route(i, j, 0, (i, j), 1)

    print('#{} {}'.format(tc, max_cnt))