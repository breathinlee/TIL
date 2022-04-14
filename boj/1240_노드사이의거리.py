#pypy3 로 통과

import sys
input = sys.stdin.readline

def dfs(start, end, total):
    if start == end:
        print(total)

    for w in range(1, N+1):
        if graph[start][w] and not visited[w]:
            visited[w] = 1
            dfs(w, end, total + graph[start][w])
            visited[w] = 0


N, M = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(N-1):
    a, b, dist = map(int, input().split())
    graph[a][b] = dist
    graph[b][a] = dist

for _ in range(M):
    start, end = map(int, input().split())
    visited = [0] * (N + 1)
    visited[start] = 1
    dfs(start, end, 0)