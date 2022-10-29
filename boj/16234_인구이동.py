from collections import deque
import sys
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def moving(r, c):
    global change

    opened_countries = [(r, c)]
    visited[r][c] = 1
    queue = deque([(r, c)])
    result = earth[r][c]

    while queue:
        r, c = queue.popleft()

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]

            if 0 > nr or nr >= N or 0 > nc or nc >= N:
                continue

            if not visited[nr][nc]:
                if abs(earth[r][c] - earth[nr][nc]) < L or abs(earth[r][c] - earth[nr][nc]) > R:
                    continue

                if L <= abs(earth[r][c] - earth[nr][nc]) <= R:
                    visited[nr][nc] = 1
                    opened_countries.append((nr, nc))
                    queue.append((nr, nc))
                    result += earth[nr][nc]

    if len(opened_countries) >= 2:
        change = True
        for country in opened_countries:
            earth[country[0]][country[1]] = result // len(opened_countries)


N, L, R = map(int, input().split())
earth = [list(map(int, input().rstrip().split())) for _ in range(N)]
total = 0

while True:
    change = False
    visited = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(r%2, N, 2):
            if not visited[r][c]:
                moving(r, c)

    if not change:
        break

    total += 1

print(total)



# pypy3로만 통과
from collections import deque
import sys
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def moving(r, c):
    global change

    result = earth[r][c]
    opened_countries = [(r, c)]
    visited[r][c] = 1
    queue = deque([(r, c)])

    while queue:
        r, c = queue.popleft()

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]

            if 0 > nr or nr >= N or 0 > nc or nc >= N:
                continue

            if not visited[nr][nc]:
                if abs(earth[r][c] - earth[nr][nc]) < L or abs(earth[r][c] - earth[nr][nc]) > R:
                    continue

                if L <= abs(earth[r][c] - earth[nr][nc]) <= R:
                    visited[nr][nc] = 1
                    opened_countries.append((nr, nc))
                    result += earth[nr][nc]
                    queue.append((nr, nc))

    if len(opened_countries) >= 2:
        change = True
        for country in opened_countries:
            earth[country[0]][country[1]] = result // len(opened_countries)


N, L, R = map(int, input().split()) 
earth = [list(map(int, input().rstrip().split())) for _ in range(N)]
total = 0

while True:
    change = False
    visited = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):    # 이 부분이 다름
            if not visited[r][c]:
                moving(r, c)

    if change:
        total += 1
    else:
        break

print(total)