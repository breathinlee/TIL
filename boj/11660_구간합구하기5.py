# sol
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[[0] * (N + 1)] for _ in range(N+1)]
for r in range(1, N + 1):
    arr[r] = [0] + list(map(int, input().split()))

sum_arr = [[0] * (N + 1) for _ in range(N+1)]
for r in range(1, N + 1):
    ret = 0
    for c in range(1, N + 1):
        ret += arr[r][c]
        sum_arr[r][c] = sum_arr[r - 1][c] + ret

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = sum_arr[x2][y2] - sum_arr[x2][y1 - 1] - sum_arr[x1 - 1][y2] + sum_arr[x1 - 1][y1 - 1]

    print(result)


# sol2 (주어진 배열 크기로만 할 때)

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

sum_arr = [[0] * N for _ in range(N)]
for r in range(N):
    ret = 0
    for c in range(N):
        ret += arr[r][c]
        if r == 0: sum_arr[r][c] = ret
        else:
            sum_arr[r][c] = sum_arr[r-1][c] + ret

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 ==1 and y1 == 1: answer = sum_arr[x2-1][y2-1]
    elif x1 == 1 and y1 != 1: answer = sum_arr[x2-1][y2-1] - sum_arr[x2-1][y1-2]
    elif x1 != 1 and y1 == 1: answer = sum_arr[x2-1][y2-1] - sum_arr[x1-2][y2-1]
    else:
        answer = sum_arr[x2-1][y2-1] - sum_arr[x2-1][y1-2] - sum_arr[x1-2][y2-1] + sum_arr[x1-2][y1-2]
    print(answer)


# pypy3로 통과 (속도 느림..)

from sys import stdin

n, m = map(int, stdin.readline().split())
arr = []
for i in range(n):
    data = list(map(int, stdin.readline().split()))
    for j in range(1, n):
        data[j] += data[j-1]
    arr.append(data)

for _ in range(m):
    res = 0
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    for i in range(x1-1, x2):
        if y1 - 2 > -1:
            res += (arr[i][y2-1] - arr[i][y1-2])
        else:
            res += (arr[i][y2-1])

    print(res)