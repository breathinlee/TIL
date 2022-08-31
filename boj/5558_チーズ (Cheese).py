# pypy로 통과

from collections import deque
import sys
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(visited):
    global start_r, start_c, power, min_time

    queue = deque([(start_r, start_c, 0)])
    visited[start_r][start_c] = 1

    while queue:
        r, c, t = queue.popleft()

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]

            if 0 <= nr < H and 0 <= nc < W:
                if board[nr][nc] != 'X' and board[nr][nc] != '.' and board[nr][nc] != 'S':
                    if power >= board[nr][nc]:
                        power += 1
                        board[nr][nc] = '.'
                        min_time += t+1
                        start_r, start_c = nr, nc
                        return
                if visited[nr][nc] or board[nr][nc] == 'X':
                    continue
                visited[nr][nc] = 1
                queue.append((nr, nc, t + 1))


H, W, N = map(int, input().split())
board = [list(input().rstrip()) for _ in range(H)]
power = 1
min_time = 0
start_r, start_c = 0, 0

for r in range(H):
    for c in range(W):
        if board[r][c] != '.' and board[r][c] != 'S' and board[r][c] != 'X':
            board[r][c] = int(board[r][c])

        elif board[r][c] == 'S':
            start_r, start_c = r, c

for _ in range(N):
    visited = [[0] * W for _ in range(H)]
    bfs(visited)

print(min_time)