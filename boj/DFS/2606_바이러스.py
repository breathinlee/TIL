# 인접행렬

def dfs(v):
    global cnt
    visited[v] = 1
    for w in range(V+1):
        if G[v][w] and not visited[w]:
            cnt += 1
            dfs(w)

    return cnt


V = int(input())
E = int(input())
G = [[0] * (V+1) for _ in range(V+1)]   # 인접행렬 생성
visited = [0] * (V+1)
cnt = 0
for _ in range(E):
    a, b = map(int, input().split())
    G[a][b] = 1
    G[b][a] = 1

print(dfs(1))


# 인접리스트

import sys

input = sys.stdin.readline

def check(node):
    global cnt

    visited[node] = 1

    for w in graph[node]:
        if not visited[w]:
            cnt += 1
            check(w)


N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
visited = [0] * (N+1)
check(1)

print(cnt)
