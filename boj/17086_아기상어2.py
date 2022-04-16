from collections import deque

dr = [1, 1, 1, -1, -1, -1, 0, 0]
dc = [0, 1, -1, 1, -1, 0, 1, -1]

N, M = map(int, input().split())
spaces = [list(map(int, input().split())) for _ in range(N)]
queue = deque()

for r in range(N):
    for c in range(M):
        if spaces[r][c]:
            queue.append((r, c))

while queue:
    r, c = queue.popleft()

    for k in range(8):
        nr = r + dr[k]
        nc = c + dc[k]

        if 0 <= nr < N and 0 <= nc < M:
            if not spaces[nr][nc]:
                spaces[nr][nc] = spaces[r][c] + 1
                queue.append((nr, nc))

result = 0
for k in range(N):
    result = max(result, max(spaces[k]))

print(result - 1)