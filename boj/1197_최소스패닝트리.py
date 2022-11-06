from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def prim():
    global ans
    heap = []
    heappush(heap, (0, 1))
    while heap:
        w, v = heappop(heap)
        if not visited[v]:
            ans += w
            visited[v] = 1
            for w, weight in G[v]:
                if not visited[w]:
                    heappush(heap, (weight, w))
    return ans


V, E = map(int, input().split())
G = [[] for _ in range(V+1)]
ans = 0
visited = [0] * (V+1)
for i in range(E):
    start, end, W = map(int, input().rstrip().split())
    G[start].append([end, W])
    G[end].append([start, W])

print(prim())