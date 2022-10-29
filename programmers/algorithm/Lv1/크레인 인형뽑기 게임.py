from collections import deque

def solution(board, moves):
    answer = 0
    N = len(board)
    moves = deque(moves)
    result = []

    while moves:
        m = moves.popleft()

        for i in range(N):
            if board[i][m-1] != 0:
                if len(result) >= 1 and result[-1] == board[i][m-1]:
                    result.pop()
                    answer += 2
                else:
                    result.append(board[i][m-1])

                board[i][m-1] = 0
                break

    return answer