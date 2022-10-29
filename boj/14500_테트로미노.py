import sys
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def dfs(r, c, value, step):
    global total

    if step == 3:
        total = max(total, value)
        return

    if value + (3 - step) * max_val <= total:
        return

    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]

        if 0 > nr or nr >= N or 0 > nc or nc >= M:
            continue

        if not visited[nr][nc]:
            if step == 1:
                visited[nr][nc] = 1
                dfs(r, c, value + arr[nr][nc], step + 1)
                visited[nr][nc] = 0

            visited[nr][nc] = 1
            dfs(nr, nc, value + arr[nr][nc], step + 1)
            visited[nr][nc] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
max_val = max(map(max, arr))
total = 0

for r in range(N):
    for c in range(M):
        visited[r][c] = 1
        dfs(r, c, arr[r][c], 0)
        visited[r][c] = 0

print(total)