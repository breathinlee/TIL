import sys
sys.stdin = open('input.txt')

# 1은 N극 성질을 가지는 자성체
# 2는 S극 성질을 가지는 자성체

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for j in range(100):
        stack = []
        for i in range(100):
            if arr[i][j] == 1:
                stack.append(arr[j][i])
            elif arr[i][j] == 2 and stack:
                cnt += 1
                stack.clear()

    print('#{} {}'.format(tc, cnt))













"""
#1 471
#2 446
#3 469
#4 481
#5 481
#6 501
#7 488
#8 476
#9 464
#10 490
"""