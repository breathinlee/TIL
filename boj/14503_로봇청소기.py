from collections import deque
import sys

input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(r, c, d):
    queue = deque([(r, c, d)])
    cnt = 1

    while queue:
        r, c, d = queue.popleft()
        nd = d

        for k in range(4):
            nd = (nd + 3) % 4
            nr = r + dr[nd]
            nc = c + dc[nd]

            if 0 <= nr < N and 0 <= nc < M and not arr[nr][nc]:
                queue.append((nr, nc, nd))
                cnt += 1
                arr[nr][nc] = -1
                break

            elif k == 3:
                back_d = (d + 2) % 4
                back_r = r + dr[back_d]
                back_c = c + dc[back_d]

                if arr[back_r][back_c] == 1:
                    return cnt

                queue.append((back_r, back_c, d))


N, M = map(int, input().split())
r, c, d = map(int, input().split())  # 0 북 1 동 2 남 3 서
arr = [list(map(int, input().split())) for _ in range(N)]

arr[r][c] = -1
print(bfs(r, c, d))