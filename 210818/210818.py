# 인접 행렬
V, E = map(int, input().split())      # 정점수, 간선수

G = [[0] * (V + 1) for _ in range(V+1)]
for _ in range(E):
    u, v = map(int, input().split())
    G[u][v] = G[v][u] = 1

for lst in G[1:]:
    print(*lst[1:])
   

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


# 인접리스트
V, E = map(int, input().split()) 

G = [[] for _ in range(V+1)]
for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

for i in range(1, V+1):
    print(i, '-->', G[i])
