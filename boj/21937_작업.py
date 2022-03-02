import sys
sys.setrecursionlimit(10**6)

def solve(v):
    global result

    visited[v] = 1

    if G[v]:
        for w in G[v]:
            if not visited[w]:
                result += 1
                solve(w)


N, M = map(int, sys.stdin.readline().split())
G = [[] for _ in range(N+1)]
visited = [0] * (N+1)
result = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    G[b].append(a)
today = int(sys.stdin.readline())

solve(today)

print(result)