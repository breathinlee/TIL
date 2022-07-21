import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    heapq.heappush(heap, (int(input())))
result = 0

while len(heap) > 1:
    a, b = heapq.heappop(heap), heapq.heappop(heap)
    result += a + b
    heapq.heappush(heap, a + b)

print(result)