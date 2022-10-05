from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    queue = deque([home])
    while queue:
        start = queue.popleft()

        if abs(start[0] - festival[0]) + abs(start[1] - festival[1]) <= 1000:
            return True

        for k in range(N):
            if not visited[k]:
                next = stores[k]
                if abs(start[0] - next[0]) + abs(start[1] - next[1]) <= 1000:
                    queue.append(next)
                    visited[k] = 1

    return False


T = int(input())
for _ in range(T):
    N = int(input())
    home = tuple(map(int, input().split()))
    stores = [tuple(map(int, input().split())) for _ in range(N)]
    festival = tuple(map(int, input().split()))

    visited = [0] * (N+1)

    if bfs():
        print('happy')
    else:
        print('sad')