def solve():
    # 행과 열
    for i in range(9):
        row = set()
        col = set()
        for j in range(9):
            row.add(arr[i][j])
            col.add(arr[j][i])
        if len(row) != 9:
            return 0
        if len(col) != 9:
            return 0

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            cnt = set()
            for k in range(3):
                for s in range(3):
                    cnt.add(arr[i + k][j + s])
            if len(cnt) != 9:
                return 0
    return 1


T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    print('#{} {}'.format(tc, solve()))