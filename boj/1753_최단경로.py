from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def dijkstra():
    heap = []
    heappush(heap, (0, K))

    while heap:
        w, now = heappop(heap)
        if dist[now] < w:
            continue
        for weight, next_node in graph[now]:
            if dist[next_node] > w + weight:
                dist[next_node] = w + weight
                heappush(heap, (w + weight, next_node))


V, E = map(int, input().split())
K = int(input())
INF = int(1e10)
graph = [[] * (V+1) for _ in range(V+1)]
dist = [INF] * (V+1)
dist[K] = 0
for _ in range(E):
    start, end, w = map(int, input().rstrip().split())
    graph[start].append((w, end))

dijkstra()

for s in range(1, V+1):
    print(dist[s]) if dist[s] != INF else print('INF')