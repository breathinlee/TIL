# 인접리스트

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(node):
    visited[node] = 1

    for w in G[node]:
        if not visited[w]:
            dfs(w)

N, M = map(int, input().split())
G = [[] * (N+1) for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
        
visited = [0] * (N+1)
cnt = 0

for v in range(1, N+1):
    if not visited[v]:
        dfs(v)
        cnt += 1

print(cnt)