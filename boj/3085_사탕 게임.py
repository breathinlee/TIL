import sys

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def get_maximum_candy(r, c):
    answer = 0

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]

        if 0 <= nr < N and 0 <= nc < N:
            count_row = 1
            count_col = 1
            board[nr][nc], board[r][c] = board[r][c], board[nr][nc]

            # 행 기준 좌우 확인
            for i in range(r-1, -1, -1):
                if board[r][c] == board[i][c]:
                    count_row += 1
                else: break

            for i in range(r+1, N):
                if board[r][c] == board[i][c]:
                    count_row += 1
                else: break

            # 열 기준 위 아래 확인
            for j in range(c - 1, -1, -1):
                if board[r][c] == board[r][j]:
                    count_col += 1
                else: break

            for j in range(c + 1, N):
                if board[r][c] == board[r][j]:
                    count_col += 1
                else: break

            answer = max(answer, count_row, count_col)
            board[nr][nc], board[r][c] = board[r][c], board[nr][nc]

    return answer


N = int(sys.stdin.readline())
board = [list(sys.stdin.readline()) for _ in range(N)]
result = 1

for r in range(N):
    for c in range(N):
        result = max(result, get_maximum_candy(r, c))

print(result)