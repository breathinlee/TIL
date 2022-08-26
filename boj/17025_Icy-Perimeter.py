from collections import deque
import sys
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def check(r, c):
    visited[r][c] = 1
    queue = deque([(r, c)])
    c_area, c_perimeter = 1, 0

    while queue:
        r, c = queue.popleft()

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]

            if 0 > nr or nr >= N or 0 > nc or nc >= N or board[nr][nc] == '.':
                c_perimeter += 1
            else:
                if not visited[nr][nc]:
                    visited[nr][nc] = 1
                    queue.append((nr, nc))
                    c_area += 1

    return c_area, c_perimeter


N = int(input())
board = [list(input()) for _ in range(N)]
area = 0
perimeter = 987654321
visited = [[0] * N for _ in range(N)]

for r in range(N):
    for c in range(N):
        if board[r][c] == '#' and not visited[r][c]:
            a, p = check(r, c)

            if a > area:
                area, perimeter = a, p
            elif a == area:
                perimeter = min(perimeter, p)

print(area, perimeter)