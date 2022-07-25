import sys
input = sys.stdin.readline

H, W, X, Y = map(int, input().split())
B_board = [list(map(int, input().split())) for _ in range(H+X)]
A_board = [[0] * W for _ in range(H)]

for h in range(H):
    for w in range(W):
        if h == 0 or w == 0:
            A_board[h][w] = B_board[h][w]
        elif h - X < 0 or w - Y < 0:
            A_board[h][w] = B_board[h][w]
        else:
            A_board[h][w] = B_board[h][w] - A_board[h-X][w-Y]

for h in range(H):
    for w in range(W):
        print(A_board[h][w], end=" ")
    print()