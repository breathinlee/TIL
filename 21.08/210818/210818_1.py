V, E = map(int, input().split())      # 정점수, 간선수

G = [[0] * (V + 1) for _ in range(V+1)]
for _ in range(E):
    u, v = map(int, input().split())
    G[u][v] = G[v][u] = 1

visited = [0] * (V+1)

# 재귀 호출 사용
def dfs(v):      # v : 현재 방문하는 정점
    visited[v] = 1
    print(v, end=' ')
    # 방문하지 않은 인접정점을 찾는다.
    for w in range(1, V+1):
        if G[v][w] == 1 and not visited[w]:
            dfs(w)

dfs(1)

"""
7 8
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7
"""