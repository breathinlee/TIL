check = [[0]*100 for _ in range(100)]
for _ in range(4):
    rectangle = list(map(int, input().split()))
    # left_edge = (rectangle[0], rectangle[1])
    # right_edge = (rectangle[2], rectangle[3])
    for i in range(rectangle[0], rectangle[2]):
        for j in range(rectangle[1], rectangle[3]):
            if check[i][j] == 0:
                check[i][j] = 1
            elif check[i][j] == 1:
                continue
cnt = 0
for r in range(100):
    for c in range(100):
        if check[r][c] == 1:
            cnt += 1

print(cnt)