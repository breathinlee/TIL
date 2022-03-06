import heapq
import sys

def dijkstra(start):
    heap = []
    dist[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        price, location = heapq.heappop(heap)

        if dist[location] < price:
            continue

        for k in info[location]:
            cost = price + k[1]

            if cost < dist[k[0]]:
                dist[k[0]] = cost
                heapq.heappush(heap, (cost, k[0]))

    return dist[end]


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
info = [[] for _ in range(N+1)]
for k in range(M):
    start, end, price = map(int, sys.stdin.readline().split())
    info[start].append([end, price])

start, end = map(int, sys.stdin.readline().split())

dist = [987654321] * (N+1)

print(dijkstra(start))


# 시간초과
import heapq
import sys


def dijkstra(start):
    heap = []
    dist[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        price, location = heapq.heappop(heap)

        if dist[location] < price:
            continue

        for k in range(M):
            if info[k][0] == location:
                cost = price + info[k][2]

                if cost < dist[info[k][1]]:
                    dist[info[k][1]] = cost
                    heapq.heappush(heap, (cost, info[k][1]))

    return dist[end]


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
info = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]  #출발지 도착지 비용
start, end = map(int, sys.stdin.readline().split())

dist = [987654321] * (N+1)

print(dijkstra(start))