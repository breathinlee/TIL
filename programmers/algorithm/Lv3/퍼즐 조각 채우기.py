from copy import deepcopy

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def rotate(arr):
    n = len(arr)
    rotated_arr = [[0] * n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            rotated_arr[c][n-r-1] = arr[r][c]

    return rotated_arr


def dfs(arr, r, c, position, check):
    n = len(arr)
    ret = [position]

    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]

        if nr < 0 or nr >= n or nc < 0 or nc >= n:
            continue

        if arr[nr][nc] == check:
            arr[nr][nc] = 2
            ret += dfs(arr, nr, nc, [position[0] + dr[k], position[1] + dc[k]], check)

    return ret


def solution(game_board, table):
    answer = 0
    n = len(game_board)
    blank = []

    for r in range(n):
        for c in range(n):
            if game_board[r][c] == 0:
                game_board[r][c] = 2
                blank.append(dfs(game_board, r, c, [0, 0], 0))

    for k in range(4):
        table = rotate(table)
        copy_rotated_table = deepcopy(table)
        for r in range(n):
            for c in range(n):
                if copy_rotated_table[r][c] == 1:
                    copy_rotated_table[r][c] = 2
                    block = dfs(copy_rotated_table, r, c, [0, 0], 1)

                    if block in blank:
                        blank.remove(block)
                        answer += len(block)
                        table = deepcopy(copy_rotated_table)

                    else:
                        copy_rotated_table = deepcopy(table)

    return answer