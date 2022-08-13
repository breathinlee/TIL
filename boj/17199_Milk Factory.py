import sys
input = sys.stdin.readline

def dfs(node):
    visited[node] = 1

    if distances[node]:
        for k in distances[node]:
            if not visited[k]:
                visited[k] = 1
                dfs(k)


N = int(input())
distances = [[] for _ in range(N+1)]
answer = -1

for _ in range(N-1):
    a, b = map(int, input().split())
    distances[b].append(a)

for i in range(1, N+1):
    visited = [0] * (N+1)
    dfs(i)

    for j in range(1, N+1):
        if not visited[j]:
            break

    else:
        answer = i
        break

print(answer)