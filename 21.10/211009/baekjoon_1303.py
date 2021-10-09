from collections import deque

def bfs(r, c, color):
    cnt = 0
    queue = deque()
    queue.append((r, c))
    visited[r][c] = 1
    while queue:
        (r, c) = queue.popleft()
        cnt += 1
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < M and 0 <= nc < N and not visited[nr][nc]:
                if G[nr][nc] == color:
                    visited[nr][nc] = 1
                    queue.append((nr, nc))

    return cnt * cnt

N, M = map(int, input().split())
G = [input() for _ in range(M)]
visited = [[0] * N for _ in range(M)]  # M행 N열
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
white_power, blue_power = 0, 0


for i in range(M):
    for j in range(N):
        if G[i][j] == 'W' and not visited[i][j]:
            white_power += bfs(i, j, 'W')

        elif G[i][j] == 'B' and not visited[i][j]:
            blue_power += bfs(i, j, 'B')

print(white_power, blue_power)