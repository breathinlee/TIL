"""
dfs - 인접행렬 반복
dfs는 시작 저점의 한 방향으로 갈 수 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 곳이 없으면,
가장 마지막에 만났던 (갈림길 간선이 있는) 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 반복하여
결국 모든 정점을 방문하는 순회방법
"""
# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

def dfs(v):
    stack = [v]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            print(v, end=' ')
            for w in range(1, V + 1):
                if G[v][w] == 1 and not visited[w]:
                    stack.append(w)


import sys
sys.stdin = open('input.txt')

V, E = map(int, input().split())
temp = list(map(int, input().split()))
G = [[0] * (V+1) for _ in range(V+1)]
visited = [0] * (V+1)

for i in range(E):
    G[temp[2*i]][temp[2*i+1]] = 1
    G[temp[2*i+1]][temp[2*i]] = 1

dfs(1)

# 1 3 7 6 5 2 4