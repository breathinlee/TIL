# 인접행렬

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(v):
    visited[v] = 1

    for w in range(1, N+1):
        if G[v][w] and not visited[w]:
            dfs(w)

N, M = map(int, input().split())
G = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 0
for _ in range(M):
    u, v = map(int, input().split())
    G[u][v] = G[v][u] = 1

for node in range(1, N+1):
    if not visited[node]:
        dfs(node)
        cnt += 1

print(cnt)