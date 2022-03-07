from collections import deque
import sys

def solve(v):
    queue = deque([v])
    destination = [0] * N

    while queue:
        tmp = queue.popleft()
        if graph[tmp]:
            for w in graph[tmp]:
                if not destination[w]:
                    queue.append(w)
                    destination[w] = 1

    return destination


N = int(sys.stdin.readline())
graph = [[] for _ in range(N)]

for r in range(N):
    G = list(map(int, sys.stdin.readline().split()))
    for c in range(N):
        if G[c]:
            graph[r].append(c)

for v in range(N):
    ans = solve(v)
    print(*ans)