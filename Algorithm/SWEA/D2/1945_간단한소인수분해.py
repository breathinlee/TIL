T = int(input())

for tc in range(1, T+1):
    N = int(input())
    prime_numbers = [2, 3, 5, 7, 11]
    prime_cnt = [0] * 5

    for i in range(5):
        while N % prime_numbers[i] == 0:
            prime_cnt[i] += 1
            N //= prime_numbers[i]

    print('#{}'.format(tc), end=' ')
    print(*prime_cnt)

"""
10
6791400
1646400
1425600
8575
185625
6480
1185408
6561
25
330750
"""

# 0812_swea_4836 색칠하기

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    box = [[0] * 10 for _ in range(10)]

    for i in range(N):
        for j in range(area[i][0], area[i][2] + 1):
            for k in range(area[i][1], area[i][3] + 1):
                box[j][k] += area[i][4]

    cnt = 0
    for s in range(10):
        for t in range(10):
            if box[s][t] >= 3:
                cnt += 1

    print('#{} {}'.format(tc, cnt))

"""
3
2
2 2 4 4 1
3 3 6 6 2
3
1 2 3 3 1
3 6 6 8 1
2 3 5 6 2
3
1 4 8 5 1
1 8 3 9 1
3 2 5 8 2
"""