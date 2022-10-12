from collections import deque
import sys
input = sys.stdin.readline

dr = [2, 2, 1, -1, -2, -2, -1, 1]
dc = [-1, 1, 2, 2, 1, -1, -2, -2]

def bfs(r, c):
    queue = deque([(r, c)])
    visited[r][c] = 1

    while queue:
        r, c = queue.popleft()
        
        if r == e1 and c == e2:
            return visited[e1][e2] - 1

        for k in range(8):
            nr, nc = r + dr[k], c + dc[k]

            if 0 > nr or nr >= I or 0 > nc or nc >= I:
                continue

            if not visited[nr][nc]:
                visited[nr][nc] = visited[r][c] + 1
                queue.append((nr, nc))

    return visited[e1][e2] - 1


T = int(input())
for _ in range(T):
    I = int(input())
    s1, s2 = map(int, input().split())
    e1, e2 = map(int, input().split())
    visited = [[0] * I for _ in range(I)]
    print(bfs(s1, s2))
