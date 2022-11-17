from collections import deque
import sys
input = sys.stdin.readline

def bfs(node):
    global far_node, max_diameter

    visited = [0] * (n+1)
    visited[node] = 1
    queue = deque([(node, 0)])

    while queue:
        next_node, weight = queue.popleft()

        if weight > max_diameter:
            max_diameter = weight
            far_node = next_node

        for child, w in graph[next_node]:
            if not visited[child]:
                queue.append((child, weight + w))
                visited[child] = 1


n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    parent, child, weight = map(int, input().rstrip().split())
    graph[child].append((parent, weight))
    graph[parent].append((child, weight))

far_node, max_diameter = 0, 0
bfs(1)

max_diameter = 0
bfs(far_node)

print(max_diameter)