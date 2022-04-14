# sol 1

from collections import deque
import sys

input = sys.stdin.readline

def bfs(start, end):
    queue = deque([(start, 0)])

    while queue:
        node, total = queue.popleft()

        if node == end:
            return total

        for k in graph[node]:
            if not visited[k[0]]:
                visited[k[0]] = 1
                queue.append((k[0], total + k[1]))


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(N-1):
    a, b, dist = map(int, input().split())
    graph[a].append((b, dist))
    graph[b].append((a, dist))

for _ in range(M):
    start, end = map(int, input().split())
    visited = [0] * (N + 1)
    visited[start] = 1
    print(bfs(start, end))



# sol2
# pypy3로 통과

from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, end):
    queue = deque([(start, 0)])

    while queue:
        node, total = queue.popleft()

        if node == end:
            return total

        for k in range(1, N+1):
            if graph[node][k] and not visited[k]:
                visited[k] = 1
                queue.append((k, total + graph[node][k]))


N, M = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(N-1):
    a, b, dist = map(int, input().split())
    graph[a][b] = graph[b][a] = dist

for _ in range(M):
    start, end = map(int, input().split())
    visited = [0] * (N + 1)
    visited[start] = 1
    print(bfs(start, end))



# sol3
# pypy3로 통과

import sys
input = sys.stdin.readline

def dfs(start, end, total):
    if start == end:
        print(total)

    for w in range(1, N+1):
        if graph[start][w] and not visited[w]:
            visited[w] = 1
            dfs(w, end, total + graph[start][w])
            visited[w] = 0


N, M = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(N-1):
    a, b, dist = map(int, input().split())
    graph[a][b] = dist
    graph[b][a] = dist

for _ in range(M):
    start, end = map(int, input().split())
    visited = [0] * (N + 1)
    visited[start] = 1
    dfs(start, end, 0)