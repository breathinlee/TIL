# dfs
import sys
sys.setrecursionlimit(10 ** 6)

dr = [1, -1, 0, 0, 1, -1, 1, -1]
dc = [0, 0, 1, -1, -1, 1, 1, -1]


def dfs(r, c):
    global flag
    
    for k in range(8):
        nr = r + dr[k]
        nc = c + dc[k]

        if 0 <= nr < N and 0 <= nc < M:
            if farm[nr][nc] > farm[r][c]:
                flag = False
            if not visited[nr][nc] and farm[nr][nc] == farm[r][c]:
                visited[nr][nc] = 1
                dfs(nr, nc)


N, M = map(int, sys.stdin.readline().split())
farm = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
cnt = 0

for r in range(N):
    for c in range(M):
        if not visited[r][c]:
            flag = True
            dfs(r, c)
            if flag: cnt += 1

print(cnt)



# bfs

import sys
from collections import deque

dr = [1, -1, 0, 0, 1, -1, 1, -1]
dc = [0, 0, 1, -1, -1, 1, 1, -1]

def bfs(r, c):
    global flag

    queue = deque([(r, c)])

    while queue:
        r, c = queue.popleft()

        for k in range(8):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < N and 0 <= nc < M:
                if farm[nr][nc] > farm[r][c]:
                    flag = False
                if not visited[nr][nc] and farm[nr][nc] == farm[r][c]:
                    visited[nr][nc] = 1
                    queue.append((nr, nc))


N, M = map(int, sys.stdin.readline().split())
farm = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
cnt = 0

for r in range(N):
    for c in range(M):
        if not visited[r][c]:
            flag = True
            visited[r][c] = 1
            bfs(r, c)

            if flag: cnt += 1

print(cnt)