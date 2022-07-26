import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def dfs(r, c):
    visited[r][c] = 1

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]

        if 0 <= nr < N and 0 <= nc < N:
            if area[r][c] == area[nr][nc] and not visited[nr][nc]:
                dfs(nr, nc)


def weakness_dfs(r, c):
    weakness_visited[r][c] = 1

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]

        if 0 <= nr < N and 0 <= nc < N:
            if area[r][c] == 'R' or area[r][c] == 'G':
                if (area[nr][nc] == 'R' or area[nr][nc] == 'G') and not weakness_visited[nr][nc]:
                    weakness_dfs(nr, nc)
            else:
                if area[r][c] == area[nr][nc] and not weakness_visited[nr][nc]:
                    weakness_dfs(nr, nc)


N = int(input())
area = list(input().rstrip() for _ in range(N))

cnt = 0
weakness_cnt = 0

visited = [[0] * N for _ in range(N)]
weakness_visited = [[0] * N for _ in range(N)]

for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            dfs(r, c)
            cnt += 1

        if not weakness_visited[r][c]:
            weakness_dfs(r, c)
            weakness_cnt += 1

print(cnt, weakness_cnt)