def bfs(v):
    Q = []
    Q.append(v)
    visited[v] = 1
    print('방문 정점: {}, 방문 체크: {}'.format(v, visited))

    while Q:
        v = Q.pop()
        for w in range(1, V+1):
            if G[w][v] and not visited[w]:
                Q.append(w)
                visited[w] = 1
                print('방문 정점: {}, 방문 체크: {}'.format(w, visited))


V, E = map(int, input().split())
temp = list(map(int, input().split()))    
G = [[0] * (V+1) for _ in range(V+1)]

for i in range(E):
    n1, n2 = temp[2*i], temp[2*i+1]
    G[n1][n2] = 1
    G[n2][n1] = 1

visited = [0] * (V+1)

bfs(1)

# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7