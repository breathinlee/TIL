from collections import deque
import sys
input = sys.stdin.readline

d = [[0, 0, 1], [0, 0, -1], [-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0]]

def bfs(tomato):
    queue = deque([])

    for h, r, c in tomato:
        queue.append((h, r, c))

    while queue:
        h, r, c = queue.popleft()

        for k in range(6):
            nh, nr, nc = h + d[k][0], r + d[k][1], c + d[k][2]

            if nh < 0 or nh >= H or nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            if box[nh][nr][nc] == 0:
                box[nh][nr][nc] = box[h][r][c] + 1
                queue.append((nh, nr, nc))


M, N, H = map(int, input().split())
box = []
for _ in range(H):
    arr = [list(map(int, input().split())) for _ in range(N)]
    box.append(arr)

answer = 0
tomato = []

for z in range(H):
    for y in range(N):
        for x in range(M):
            if box[z][y][x] == 1:
                tomato.append((z, y, x))

bfs(tomato)

flag = False

for i in box:
    for j in i:
        if 0 in j:
            answer = -1
            flag = True
            break

if not flag:
    for i in box:
        for j in i:
            if answer < max(j):
                answer = max(j) - 1

print(answer)