# 100점

import sys
input = sys.stdin.readline

M, N = map(int, input().split())
worms = [1] * (2 * M)

# 해당 수가 증가해야하는 시작 인덱스에 수를 배치
for _ in range(N):
    a, b, c = map(int, input().split())
    worms[a] += 1
    worms[a + b] += 1

cnt = 0
for k in range(2*M-1):
    worms[k] += cnt
    cnt = worms[k] - 1

for i in range(M - 1, -1, -1):
    print(*([worms[i]] + worms[M:-1]))



# 83점 (1)

import sys
input = sys.stdin.readline

M, N = map(int, input().split())
arr = [[1] * M for _ in range(M)]
lst = [0] * (2*M-1)

for _ in range(N):
    a, b, c = map(int, input().split())

    for k in range(a, a+b):
        lst[k] += 1

    for s in range(a+b, 2*M-1):
        lst[s] += 2

for i in range(2*M-1):
    if i < M:
        arr[M-1-i][0] += lst[i]
    elif i == M-1:
        arr[0][0] += lst[i]
    else:
        arr[0][i-M+1] += lst[i]

for i in range(1, M):
    for j in range(1, M):
        arr[i][j] = arr[0][j]

for i in range(M):
    print(" ".join(map(str, arr[i])))


# 83점 (2)

import sys
input = sys.stdin.readline

M, N = map(int, input().split())
arr = [[1] * M for _ in range(M)]
lst = [0] * (2*M-1)

for _ in range(N):
    a, b, c = map(int, input().split())

    for k in range(a, a+b):
        lst[k] += 1

    for s in range(a+b, 2*M-1):
        lst[s] += 2

for i in range(M-1, -1, -1):
    arr[i][0] += lst[M-i-1]

for j in range(1, M):
    arr[0][j] += lst[M+j-1]

    for k in range(1, M):
        arr[k][j] = arr[k-1][j]

for a in arr:
    print(*a)