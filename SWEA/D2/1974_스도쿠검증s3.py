numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def solve(arr):
    for row in arr:
        for number in numbers:
            if number not in row:
                return 0

    for i in range(9):
        col = []
        for j in range(9):
            col.append(arr[j][i])
        for number in numbers:
            if number not in col:
                return 0

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            cnt = [0] * 10
            for k in range(3):
                for s in range(3):
                    cnt[arr[i+k][j+s]] += 1
            for l in range(1, 10):
                if cnt[l] != 1:
                    return 0

    return 1


T = int(input())
for tc in range(1, T+1):
    board = [list(map(int, input().split())) for _ in range(9)]
    print('#{} {}'.format(tc, solve(board)))