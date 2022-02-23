from typing import ValuesView


def bfs(v):
    Q = [v]
    while Q:
        v = Q.pop(0)
        if v not in visited:
            visited.append(v)
            for w in G[v]:
                if w not in visited:
                    Q.append(w)
    return ' -> '.join(map(str, visited))


V, E = map(int, input().split())
temp = [list(map(int, input().split()))]
G = [[] for _ in range(V+1)]
for i in range(len(temp)//2):
    G[temp[i*2]].append(temp[2*i+1])
visited = []
print(bfs(1))

# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7