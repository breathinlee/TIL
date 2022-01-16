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