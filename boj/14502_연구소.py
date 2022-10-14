import copy
from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(lab):
    queue = deque([])
    visited = [[0] * M for _ in range(N)]

    for (r, c) in virus:
        queue.append((r, c))

    while queue:
        r, c = queue.popleft()

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]

            if 0 > nr or nr >= N or 0 > nc or nc >= M:
                continue

            if not visited[nr][nc]:
                if lab[nr][nc] == 0:
                    visited[nr][nc] = 1
                    lab[nr][nc] = 2
                    queue.append((nr, nc))


# 0 빈칸, 1 벽, 2 바이러스
N, M = map(int, input().split())
lab = []
empty = []
virus = []
for r in range(N):
    tmp = list(map(int, input().rstrip().split()))
    lab.append(tmp)
    for c in range(M):
        if tmp[c] == 2:
            virus.append((r, c))
        elif tmp[c] == 0:
            empty.append((r, c))

max_area = 0
cases = combinations(empty, 3)
for case in cases:
    case_lab = copy.deepcopy(lab)

    for (r, c) in case:
        case_lab[r][c] = 1

    bfs(case_lab)

    safe = 0
    for row in case_lab:
        safe += row.count(0)

    if safe > max_area:
        max_area = safe

print(max_area)