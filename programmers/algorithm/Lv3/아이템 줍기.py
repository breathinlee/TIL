from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def bfs(start_x, start_y, target_x, target_y, arr):
    visited = [[1] * 102 for _ in range(102)]
    queue = deque([(start_y, start_x)])

    while queue:
        r, c = queue.popleft()

        if r == target_y and c == target_x:
            return visited[r][c] // 2

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]

            if visited[nr][nc] == 1 and arr[nr][nc] == 1:
                visited[nr][nc] = visited[r][c] + 1
                queue.append((nr, nc))


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    arr = [[-1] * 102 for _ in range(102)]

    for rect in rectangle:
        x1, y1, x2, y2 = rect
        nx1, ny1, nx2, ny2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2

        for r in range(ny1, ny2 + 1):
            for c in range(nx1, nx2 + 1):
                if ny1 < r < ny2 and nx1 < c < nx2:
                    arr[r][c] = 0
                elif arr[r][c] != 0:
                    arr[r][c] = 1

    answer = bfs(characterX * 2, characterY * 2, itemX * 2, itemY * 2, arr)

    return answer