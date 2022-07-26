import sys
input = sys.stdin.readline

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def white(horse_num, r, c, nr, nc, direction):
    data[horse_num] = [nr, nc, direction]

    reverse_horse = []
    while (horses[r][c][-1] != horse_num):
        tmp = horses[r][c].pop()
        reverse_horse.append(tmp)
        data[tmp][0] = nr
        data[tmp][1] = nc
    reverse_horse.append(horses[r][c].pop())
    reverse_horse.reverse()
    horses[nr][nc].extend(reverse_horse)

    return 4 if len(horses[nr][nc]) >= 4 else -1


def red(horse_num, r, c, nr, nc, direction):
    data[horse_num] = [nr, nc, direction]

    while (horses[r][c][-1] != horse_num):
        tmp = horses[r][c].pop()
        data[tmp][0] = nr
        data[tmp][1] = nc
        horses[nr][nc].append(tmp)

    horses[nr][nc].append(horses[r][c].pop())

    return 4 if len(horses[nr][nc]) >= 4 else -1


def blue(horse_num, r, c):
    if data[horse_num][2] == 0:
        data[horse_num][2] = 1
    elif data[horse_num][2] == 1:
        data[horse_num][2] = 0
    elif data[horse_num][2] == 2:
        data[horse_num][2] = 3
    else:
        data[horse_num][2] = 2

    direction = data[horse_num][2]
    nr = r + dr[direction]
    nc = c + dc[direction]

    if nr < 0 or nr >= N or nc < 0 or nc >= N or board[nr][nc] == 2:
        return -1
    elif board[nr][nc] == 1:
        return red(horse_num, r, c, nr, nc, direction)
    else:
        return white(horse_num, r, c, nr, nc, direction)


N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# 체스판에 말이 쌓인 정도를 보여주는 배열
horses = [[[] for j in range(N)] for i in range(N)]
# 체스판 말의 정보
data = []
for k in range(K):
    r, c, d = map(int, input().split())
    data.append([r-1, c-1, d-1])
    horses[r-1][c-1].append(k)

total = 0

while True:
    for k in range(K):
        r, c, d = data[k]
        ret = 0
        # 맨 아래만 움직일 수 있음
        if horses[r][c][0] != k:
            continue

        nr = r + dr[d]
        nc = c + dc[d]
        
        if nr < 0 or nr >= N or nc < 0 or nc >= N or board[nr][nc] == 2:
            ret = blue(k, r, c)
        elif board[nr][nc] == 1:
            ret = red(k, r, c, nr, nc, d)
        else:
            ret = white(k, r, c, nr, nc, d)

        if ret == 4:
            total += 1
            print(total)
            sys.exit()

    total += 1

    if total > 1000:
        break

print(-1)
