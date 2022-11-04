import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    number = int(input().rstrip())
    if number > 0:
        heapq.heappush(heap, number)
    elif number == 0:
        if len(heap):
            target = heapq.heappop(heap)
            print(target)
        else:
            print(0)