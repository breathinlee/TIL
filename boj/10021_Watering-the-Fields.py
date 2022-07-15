#pypy3로 통과

from itertools import combinations
import heapq
import sys
input = sys.stdin.readline

def find_parent(node):
    if parent[node] != node:
        parent[node] = find_parent(parent[node])
    return parent[node]


def union_parent(node1, node2):
    a, b = find_parent(node1), find_parent(node2)
    if a == b:
        return False
    else:
        parent[b] = a
        return True


N, C = map(int, input().split())
info = []
for k in range(N):
    x, y = map(int, input().split())
    info.append((k, x, y))

cases = []

for case in combinations(info, 2):
    distance = ((case[0][1] - case[1][1]) ** 2 + (case[0][2] - case[1][2]) ** 2)
    if distance >= C:
        heapq.heappush(cases, [distance, case[0][0], case[1][0]])

parent = [i for i in range(N)]
result = cnt = 0

while cases:
    value, a, b = heapq.heappop(cases)

    if union_parent(a, b):
        result += value
        cnt += 1
        if cnt == N-1:
            print(result)
            break
else:
    print(-1)