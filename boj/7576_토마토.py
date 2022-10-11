from collections import deque
import sys
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(tomato):
    queue = deque([])

    for r, c in tomato:
        queue.append((r, c))

    while queue:
        r, c = queue.popleft()

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]

            if 0 > nr or nr >= N or 0 > nc or nc >= M:
                continue

            if box[nr][nc] == 0:
                box[nr][nc] = box[r][c] + 1
                queue.append((nr, nc))


M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
answer = -1
tomato = []

for r in range(N):
    for c in range(M):
        if box[r][c] == 1:
            tomato.append((r, c))

bfs(tomato)

for r in range(N):
    if max(box[r]) > answer:
        answer = max(box[r]) -1

    if 0 in box[r]:
        answer = -1
        break

print(answer)