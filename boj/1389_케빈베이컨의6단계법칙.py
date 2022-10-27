from collections import deque
import sys
input = sys.stdin.readline

def bfs(node):
    queue = deque([node])
    distance = [0] * (N+1)
    distance[node] = 1

    while queue:
        start = queue.popleft()

        for ne in graph[start]:
            if not distance[ne]:
                distance[ne] = distance[start] + 1
                queue.append(ne)

    return sum(distance)


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

result = 1e6
bacon = 0

for k in range(1, N+1):
    if result > bfs(k):
        result = bfs(k)
        bacon = k

print(bacon)