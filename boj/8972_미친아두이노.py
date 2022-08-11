import sys
input = sys.stdin.readline

dr = [0, 1, 1, 1, 0, 0, 0, -1, -1, -1]
dc = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]

def moving(idx):
    global c_arduino

    next_arduino = set()
    bomb = set()

    for cr, cc in c_arduino:
        board[cr][cc] = '.'
        ret, d = 1e3, 0
        for s in range(1, 10):
            cnr, cnc = cr + dr[s], cc + dc[s]

            if abs(nr - cnr) + abs(nc - cnc) <= ret:
                ret = abs(nr - cnr) + abs(nc - cnc)
                d = s

        if (cr + dr[d], cc + dc[d]) == (nr, nc):
            print('{} {}'.format('kraj', idx+1))
            return False

        elif (cr + dr[d], cc + dc[d]) in next_arduino:
            bomb.add((cr + dr[d], cc + dc[d]))

        else:
            next_arduino.add((cr + dr[d], cc + dc[d]))

    if len(bomb):
        for x, y in bomb:
            if (x, y) in next_arduino:
                next_arduino.remove((x, y))

    for x, y in next_arduino:
        board[x][y] = 'R'

    c_arduino = next_arduino

    return True


R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
directions = list(input().strip())
c_arduino = set()

for r in range(R):
    for c in range(C):
        if board[r][c] == 'I':
            start = (r, c)
        elif board[r][c] == 'R':
            c_arduino.add((r, c))

for idx, dir in enumerate(directions):
    dir = int(dir)

    r, c = start[0], start[1]
    nr, nc = r + dr[dir], c + dc[dir]

    if (nr, nc) in c_arduino:
        print('{} {}'.format('kraj', idx+1))
        exit()

    board[r][c] = '.'
    board[nr][nc] = 'I'
    start = (nr, nc)

    flag = moving(idx)

    if not flag:
        exit()

for r in range(R):
    print(''.join(board[r]))