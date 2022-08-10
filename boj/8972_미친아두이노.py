# 미해결

from collections import deque
import sys

dr = [0, 1, 1, 1, 0, 0, 0, -1, -1, -1]
dc = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]

def moving(start):
    global c_arduino

    while directions:
        dir = directions.popleft()

        r, c = start[0], start[1]
        nr, nc = r + dr[int(dir)], c + dc[int(dir)]

        if dir != '5' and 0 <= nr < R and 0 <= nc < C:
            if board[nr][nc] == '.':
                board[r][c] = '.'
                board[nr][nc] = 'I'
                start = (nr, nc)

            elif board[nr][nc] == 'R':
                return

        next_arduino = deque()
        bomb = set()

        while c_arduino:
            ret, d = 1e3, 0
            cr, cc = c_arduino.popleft()
            for s in range(1, 10):
                cnr, cnc = cr + dr[s], cc + dc[s]

                if s != 5 and 0 <= cnr < R and 0 <= cnc < C:
                    if abs(nr - cnr) + abs(nc - cnc) < ret:
                        ret = abs(nr - cnr) + abs(nc - cnc)
                        d = s

            if board[cr + dr[d]][cc + dc[d]] == '.':
                next_arduino.append((cr + dr[d], cc + dc[d]))
                board[cr][cc] = '.'
                board[cr + dr[d]][cc + dc[d]] = 'R'
            elif board[cr + dr[d]][cc + dc[d]] == 'R':
                board[cr][cc] = '.'
                bomb.add((cr + dr[d], cc + dc[d]))

            elif board[cr + dr[d]][cc + dc[d]] == 'I':
                return

        if len(bomb):
            for x, y in bomb:
                if (x, y) in next_arduino:
                    next_arduino.remove((x, y))
                    board[x][y] = '.'

        c_arduino = next_arduino

    return


R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
directions = deque(list(input()))
answer = len(directions)
c_arduino = deque()

for r in range(R):
    for c in range(C):
        if board[r][c] == 'I':
            start = (r, c)
        elif board[r][c] == 'R':
            c_arduino.append((r, c))

moving(start)

if len(directions):
    print('kraj', answer - len(directions))
else:
    for r in range(R):
        print(''.join(board[r]))