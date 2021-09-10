def sudoku(arr):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            blank = []
            for k in range(3):
                for l in range(3):
                    if blank:
                        if arr[i + k][j + l] in blank:
                            return 0
                    blank.append(arr[i + k][j + l])

    for i in range(9):
        blank = []
        for j in range(9):
            if blank:
                if arr[i][j] in blank:
                    return 0
            blank.append(arr[i][j])

    for i in range(9):
        blank = []
        for j in range(9):
            if blank:
                if arr[j][i] in blank:
                    return 0
            blank.append(arr[j][i])
    return 1

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    ans = sudoku(arr)
    print('#{} {}'.format(tc, ans))
