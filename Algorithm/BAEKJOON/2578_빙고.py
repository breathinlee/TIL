def check_bingo(arr):
    cnt = 0
    # 가로 체크
    for r in arr:
        if r.count(0) == 5:
            cnt += 1

    # 세로 체크
    for i in range(5):
        ret = 0
        for j in range(5):
            if arr[j][i] == 0:
                ret += 1
        if ret == 5:
            cnt += 1

    # 대각선 체크
    sum3, sum4 = 0, 0
    for k in range(5):
        sum3 += arr[k][k]
        sum4 += arr[k][4-k]
    if sum3 == 0:
        cnt += 1
    if sum4 == 0:
        cnt += 1

    return cnt

cheolsu_board = [list(map(int, input().split())) for _ in range(5)]
calling_numbers = list(map(int, input().split()))
for _ in range(4):
    calling_numbers += list(map(int, input().split()))
ans = 0

for number in calling_numbers:
    for i in range(5):
        for j in range(5):
            if cheolsu_board[i][j] == number:
                cheolsu_board[i][j] = 0

    if check_bingo(cheolsu_board) >= 3:
        ans = calling_numbers.index(number)
        break

print(ans + 1)