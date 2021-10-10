"""
dfs - 인접행렬 재귀
"""

def dfs(v):
    # if not visited[v]:
    visited[v] = 1
    print(v, end=' ')
    for w in range(1, V+1):
        if G[v][w] and not visited[w]:
            dfs(w)                    # 시작 정점으로 다 올라오면 함수 종료

# from pandas import DataFrame
import sys
sys.stdin = open('input.txt')

V, E = map(int, input().split())
temp = list(map(int, input().split()))
G = [[0] * (V+1) for _ in range(V+1)]

visited = [0] * (V+1)
for i in range(V+1):
    G[temp[i*2]][temp[i*2+1]] = 1
    G[temp[i*2+1]][temp[i*2]] = 1

# print(DataFrame(G))

dfs(1)

# 1 2 4 6 5 7 3