#pypy3로 통과...

from collections import deque
import sys

input = sys.stdin.readline

def bfs(node):
    global answer, max_node

    queue = deque([node])
    visited[node] = 1
    ret = 1

    while queue:
        tmp = queue.popleft()

        for w in graph[tmp]:
            if not visited[w]:
                queue.append(w)
                visited[w] = 1
                ret += 1

    return ret


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
max_node = []
answer = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

cnt = [0] * (N+1)
for n in range(1, N+1):
    if graph[n]:
        visited = [0] * (N+1)
        cnt[n] = bfs(n)

max_val = max(cnt)
for idx, val in enumerate(cnt):
    if max_val == val:
        print(idx, end=' ')