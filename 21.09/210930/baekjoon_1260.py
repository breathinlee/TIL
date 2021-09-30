def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for w in range(1, N+1):
        if G[v][w] and not visited[w]:
            dfs(w)

def bfs(v):
    visited = [0] * (N + 1)
    queue = [v]
    while queue:
        v = queue.pop(0)
        if not visited[v]:
            visited[v] = 1
            print(v, end=' ')
            for w in range(1, N+1):
                if G[v][w] and not visited[w]:
                    queue.append(w)

N, M, V = map(int, input().split())
G = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    G[a][b] = 1
    G[b][a] = 1


dfs(V)
print()
bfs(V)