# sol 1 - permutations 이용 (176ms)
from itertools import permutations
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
gain_Weight = list(map(int, input().strip().split()))
result = 0

cases = permutations([i for i in range(N)], N)
for case in cases:
    total = 500
    for c in case:
        if total + gain_Weight[c] - K < 500:
            break
        else:
            total = total + gain_Weight[c] - K
    else:
        result += 1

print(result)


# sol 2 - 백트래킹 이용 (140ms)
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
gain_Weight = list(map(int, input().strip().split()))
result = 0

def dfs(visited, weight):
    global result

    if all(visited):
        result += 1
        return

    for i in range(N):
        if not visited[i]:
            tmp = weight + gain_Weight[i] - K
            if tmp < 500:
                continue
            visited[i] = 1
            dfs(visited, tmp)
            visited[i] = 0

visited = [0] * N
weight = 500
dfs(visited, weight)

print(result)