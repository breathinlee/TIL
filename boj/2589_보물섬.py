# pypy3로 통과

from collections import deque
import sys
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(r, c):
    queue = deque([(r, c, 0)])
    visited = [[0] * width for _ in range(height)]
    visited[r][c] = 1
    total = 0

    while queue:
        r, c, move = queue.popleft()
        if total < move:
            total = move

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]

            if 0 > nr or nr >= height or 0 > nc or nc >= width:
                continue

            if not visited[nr][nc]:
                if treasure[nr][nc] == 'L':
                    visited[nr][nc] = 1
                    queue.append((nr, nc, move + 1))

    return total


height, width = map(int, input().split())
treasure = [list(input().rstrip()) for _ in range(height)]
result = 0

for r in range(height):
    for c in range(width):
        if treasure[r][c] == 'L':
            result = max(result, bfs(r, c))

print(result)


# python3로 통과 

from collections import deque
import sys
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(r, c):
    global result

    queue = deque([(r, c)])

    while queue:
        r, c = queue.popleft()

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]

            if 0 > nr or nr >= height or 0 > nc or nc >= width:
                continue

            if treasure[nr][nc] == 'W':
                continue

            if visited[nr][nc] == -1 and treasure[nr][nc] == 'L':
                visited[nr][nc] = visited[r][c] + 1
                queue.append((nr, nc))

                if result < visited[nr][nc]:
                    result = visited[nr][nc]


height, width = map(int, input().split())
treasure = [list(input().rstrip()) for _ in range(height)]
result = 0

for r in range(height):
    for c in range(width):
        if r - 1 >= 0 and r + 1 < height:
            if treasure[r-1][c] == 'L' and treasure[r+1][c] == 'L':
                continue

        if c - 1 >= 0 and c + 1 < width:
            if treasure[r][c-1] == 'L' and treasure[r][c+1] == 'L':
                continue

        if treasure[r][c] == 'L':
            visited = [[-1] * width for _ in range(height)]
            visited[r][c] = 0
            bfs(r, c)

print(result)
