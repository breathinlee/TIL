import sys
input = sys.stdin.readline

def dfs(start):
    if graph[start]:
        for k in graph[start]:
            if not visited[k]:
                visited[k] = visited[start] + 1
                dfs(k)


n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    r1, r2 = map(int, input().rstrip().split())
    graph[r1].append(r2)
    graph[r2].append(r1)

visited = [0] * (n+1)
dfs(p1)
print(visited[p2]) if visited[p2] else print(-1)