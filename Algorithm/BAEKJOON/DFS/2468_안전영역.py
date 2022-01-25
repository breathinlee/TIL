import sys
sys.setrecursionlimit(100000)

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def dfs(r, c, h):
    visited[r][c] = 1

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]

        if 0 <= nr < N and 0 <= nc < N:
            if not visited[nr][nc] and arr[nr][nc] > h:
                dfs(nr, nc, h)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0

for i in range(101):
    cnt = 0
    visited = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if arr[r][c] > i and not visited[r][c]:
                dfs(r, c, i)
                cnt += 1

    if result < cnt:
        result = cnt

print(result)