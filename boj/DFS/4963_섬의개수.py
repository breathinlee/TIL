import sys
sys.setrecursionlimit(10000)

dr = [1, -1, 0, 0, 1, -1, 1, -1]
dc = [0, 0, 1, -1, -1, 1, 1, -1]

def dfs(r, c):
    visited[r][c] = 1

    for k in range(8):
        nr = r + dr[k]
        nc = c + dc[k]

        if 0 <= nr < h and 0 <= nc < w:
            if map_info[nr][nc] and not visited[nr][nc]:
                dfs(nr, nc)


# 1: 땅, 0: 바다
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    map_info = [list(map(int, input().split())) for _ in range(h)]

    visited = [[0] * w for _ in range(h)]
    cnt = 0

    for r in range(h):
        for c in range(w):
            if map_info[r][c] and not visited[r][c]:
                dfs(r, c)
                cnt += 1

    print(cnt)