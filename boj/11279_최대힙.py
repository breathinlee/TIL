from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    number = int(input().rstrip())

    if number == 0:
        if len(heap):
            print(-heappop(heap))
        else:
            print(0)
    else:
        heappush(heap, -number)