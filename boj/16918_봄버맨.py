from collections import deque
import sys
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def setting_bomb():
    for r in range(R):
        for c in range(C):
            if board[r][c] != '.':
                bomb_list.append((r, c))


def install():
    for r in range(R):
        for c in range(C):
            if board[r][c] != 'O':
                board[r][c] = 'O'


def bomb():
    while bomb_list:
        bomb_r, bomb_c = bomb_list.popleft()
        board[bomb_r][bomb_c] = '.'

        for k in range(4):
            bomb_nr = bomb_r + dr[k]
            bomb_nc = bomb_c + dc[k]

            if 0 <= bomb_nr < R and 0 <= bomb_nc < C:
                board[bomb_nr][bomb_nc] = '.'


R, C, N = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
bomb_list = deque()

N -= 1
while N:
    setting_bomb()
    install()
    N -= 1

    if N == 0:
        break

    bomb()
    N -= 1

for r in range(R):
    for c in range(C):
        print(board[r][c], end='')
    print()