def shiftBoard(m, n, board):
    for _ in range(m):
        for r in range(m-1):
            for c in range(n):
                if board[r+1][c] == '0':
                    board[r+1][c], board[r][c] = board[r][c], board[r+1][c]

    return board


def bomb(m, n, board):
    removal = set()
    for r in range(m - 1):
        for c in range(n - 1):
            if board[r][c] == '0':
                pass

            elif board[r][c] == board[r][c + 1] == board[r + 1][c] == board[r + 1][c + 1]:
                removal.add((r, c))
                removal.add((r, c + 1))
                removal.add((r + 1, c))
                removal.add((r + 1, c + 1))

    return removal


def solution(m, n, board):
    answer = 0

    while True:
        ret = bomb(m, n, board)

        if len(ret):
            board = list(map(list, board))
            answer += len(ret)
            for r, c in ret:
                board[r][c] = '0'
            board = shiftBoard(m, n, board)

        else:
            return answer