# sol 1 (pypy3)

import sys
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def dfs(r, c, cnt):
    global result

    if result < cnt:
        result = cnt

    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]

        if 0 > nr or nr >= R or 0 > nc or nc >= C:
            continue

        if board[nr][nc] not in route:
            route.add(board[nr][nc])
            dfs(nr, nc, cnt + 1)
            route.remove(board[nr][nc])


R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
route = set()
route.add(board[0][0])
result = 0

dfs(0, 0, 1)

print(result)



# sol 2 (python 3)

import sys
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs():
    result = 1
    queue = set()
    queue.add((0, 0, board[0][0]))

    while queue:
        r, c, route = queue.pop()

        if result < len(route):
            result = len(route)

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]

            if 0 > nr or nr >= R or 0 > nc or nc >= C:
                continue

            if board[nr][nc] not in route:
                queue.add((nr, nc, route + board[nr][nc]))

    return result


R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]

print(bfs())