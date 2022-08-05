# sol 1 (88ms)

from itertools import combinations
import sys
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def search():
    for teacher in teachers:
        for k in range(4):
            r, c = teacher[0], teacher[1]
            while 0 <= r < N and 0 <= c < N:
                if arr[r][c] == 'O':
                    break
                elif arr[r][c] == 'S':
                    return False

                r += dr[k]
                c += dc[k]

    return True


N = int(input())
arr = []
teachers = []
empty = []
flag = False

for r in range(N):
    arr.append(list(input().split()))
    for c in range(N):
        if arr[r][c] == 'T':
            teachers.append((r, c))
        elif arr[r][c] == 'X':
            empty.append((r, c))

cases = combinations(empty, 3)

for case in cases:
    for r, c in case:
        arr[r][c] = 'O'

    if search():
        flag = True
        break

    for r, c in case:
        arr[r][c] = 'X'

if flag:
    print('YES')
else:
    print('NO')


# sol 2 (160ms)

import sys
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def search():
    for teacher in teachers:
        for k in range(4):
            r, c = teacher[0], teacher[1]

            while 0 <= r < N and 0 <= c < N:
                if arr[r][c] == 'O':
                    break
                elif arr[r][c] == 'S':
                    return False

                r += dr[k]
                c += dc[k]

    return True


def dfs(cnt):
    global flag

    if cnt == 3:
        if search():
            flag = True

        return

    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'X':
                arr[r][c] = 'O'
                cnt += 1
                dfs(cnt)
                arr[r][c] = 'X'
                cnt -= 1


N = int(input())
arr = []
teachers = []

flag = False

for r in range(N):
    arr.append(list(input().split()))

    for c in range(N):
        if arr[r][c] == 'T':
            teachers.append((r, c))

dfs(0)

print('YES' if flag else 'NO')