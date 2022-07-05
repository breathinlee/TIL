import sys
input = sys.stdin.readline

N = int(input())
info = [tuple(map(int, input().split())) for _ in range(N)]
order = [1] * N

for k in range(N):
    tmp = info[k]
    for s in info:
        if tmp[0] < s[0] and tmp[1] < s[1]:
            order[k] += 1

print(*order)