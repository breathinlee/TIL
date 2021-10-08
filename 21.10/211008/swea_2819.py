def dfs(r, c, cnt, result):
    if cnt == 6:
        if result not in numbers:
            numbers.append(result)
        return

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]

        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(nr, nc, cnt + 1, result + board[nr][nc])


T = int(input())
for tc in range(1, T+1):
    board = [list(input().split()) for _ in range(4)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    numbers = []    # 결과를 담을 배열 생성

    for i in range(4):
        for j in range(4):
            dfs(i, j, 0, board[i][j])      # 출발 위치, 횟수, 만들어진 문자열

    # numbers = set(numbers)
    print('#{} {}'.format(tc, len(numbers)))