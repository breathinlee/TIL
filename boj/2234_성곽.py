from collections import deque
import sys
input = sys.stdin.readline

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def bfs(r, c, room_number):
    area = 1
    queue = deque([(r, c)])
    room_check[r][c] = room_number

    while queue:
        r, c = queue.popleft()

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]

            if arr[r][c][k] == '0' and room_check[nr][nc] == -1:
                queue.append((nr, nc))
                room_check[nr][nc] = room_number
                area += 1

    return area


N, M = map(int, input().split())
arr = []
for _ in range(M):
    tmp = list(map(int, input().strip().split()))
    for k in range(N):
        tmp[k] = bin(tmp[k])[2:]
        if len(tmp[k]) < 4:
            tmp[k] = '0' * (4 - len(tmp[k])) + tmp[k]

    arr.append(tmp)

room_check = [[-1] * N for _ in range(M)]
rooms = []
room_number = 0
after_max_room_area = 0

for r in range(M):
    for c in range(N):
        if room_check[r][c] == -1:
            rooms.append(bfs(r, c, room_number))
            room_number += 1

for r in range(M):
    for c in range(N):
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < M and 0 <= nc < N and arr[r][c][k] == '1' and room_check[r][c] != room_check[nr][nc]:
                after_max_room_area = max(after_max_room_area, rooms[room_check[r][c]] + rooms[room_check[nr][nc]])


print(len(rooms))
print(max(rooms))
print(after_max_room_area)