"""
dfs - 인접리스트 재귀
"""

def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for w in G[v]:
        if not visited[w]:
            dfs(w)

import sys
sys.stdin = open('input.txt')

V, E = map(int, input().split())
temp = list(map(int, input().split()))
G = [[] for _ in range(V+1)]
visited = [0] * (V+1)

for i in range(len(temp)//2):
    G[temp[2*i]].append(temp[2*i+1])
    G[temp[2*i+1]].append(temp[2*i])

# print(G)
# [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]
dfs(1)