# sol1

import sys
sys.setrecursionlimit(10**6)

def dfs(r, c):
    global cnt
  
    cnt += 1
    
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]

        if 0 <= nr < N and 0 <= nc < M and garbage[nr][nc] and not visited[nr][nc]:
            visited[nr][nc] = 1
            dfs(nr, nc)
    
    return cnt


input = sys.stdin.readline
N, M, K = map(int, input().split())    # 세로 길이 N 가로 길이 M 음식물 쓰레기 개수 K
garbage = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    garbage[a-1][b-1] = 1

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
max_cnt = 0

for r in range(N):
    for c in range(M):
        if garbage[r][c] and not visited[r][c]:
            cnt = 0
            visited[r][c] = 1
            max_cnt = max(max_cnt, dfs(r, c))

print(max_cnt)


# sol2

import sys
sys.setrecursionlimit(10**6)

def dfs(r, c, cnt):
    visited[r][c] = 1

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]

        if 0 <= nr < N and 0 <= nc < M and garbage[nr][nc] and not visited[nr][nc]:
            cnt = dfs(nr, nc, cnt + 1)

    return cnt


input = sys.stdin.readline
N, M, K = map(int, input().split()) 
garbage = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    garbage[a - 1][b - 1] = 1

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
max_cnt = 0

for r in range(N):
    for c in range(M):
        if garbage[r][c] and not visited[r][c]:
            ret = dfs(r, c, 1)
            max_cnt = max(max_cnt, ret)

print(max_cnt)