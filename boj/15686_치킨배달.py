import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
city_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
house = []
chicken = []
total = 1e6

for i in range(N):
    for j in range(N):
        if city_map[i][j] == 1:
            house.append([i, j])
        elif city_map[i][j] == 2:
            chicken.append([i, j])

for c in combinations(chicken, M):
    tmp = 0
    for h in house:
        ret = 101
        for k in range(M):
            ret = min(ret, abs(h[0] - c[k][0]) + abs(h[1] - c[k][1]))
        tmp += ret

    total = min(tmp, total)

print(total)


