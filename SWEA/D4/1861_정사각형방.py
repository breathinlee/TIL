def check(r, c):
    global max_value, cnt, room_number

    queue = [(r, c)]
    while queue:
        r, c = queue.pop(0)
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == arr[r][c] + 1:
                queue.append((nr, nc))
                cnt += 1

    if cnt > max_value:
        max_value = cnt
        room_number = arr[r][c] - max_value + 1
    
    elif cnt == max_value:
        if room_number > arr[r][c]:
            room_number = arr[r][c] - max_value + 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    max_value = 0
    room_number = N*N

    for i in range(N):
        for j in range(N):
            cnt = 1
            check(i, j)

    print('#{} {} {}'.format(tc, room_number, max_value))