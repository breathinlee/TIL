from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        r, c = queue.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M:
                if field[nr][nc] == 1:
                    field[nr][nc] = 0
                    queue.append((nr, nc))


T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())    # M: 배추밭 가로길이 N: 배추밭 세로길이 K: 배추가 심어져 있는 위치 개수
    field = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    cnt = 0                                # 배추흰지렁이 수
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for _ in range(K):                     # 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)
        a, b = map(int, input().split())
        field[b][a] = 1

    for r in range(N):
        for c in range(M):
            if field[r][c] and not visited[r][c]:
                bfs(r, c)
                cnt += 1

    print(cnt)