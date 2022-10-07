from collections import deque

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def solution(maps):
    answer = 0
    N = len(maps)
    M = len(maps[0])
    
    def bfs(r, c):
        queue = deque([(r, c)])
        
        while queue:
            r, c = queue.popleft()

            for k in range(4):
                nr, nc = r + d[k][0], c + d[k][1]

                if 0 > nr or nr >= N or 0 > nc or nc >= M:
                    continue

                if maps[nr][nc] == 1:
                    maps[nr][nc] = maps[r][c] + 1
                    queue.append((nr, nc))

        return maps[N-1][M-1]
    
    answer = bfs(0, 0)
    
    if answer == 1:
        return -1
    return answer