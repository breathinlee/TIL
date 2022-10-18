import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def dfs(r, c):
    global cnt

    visited[r][c] = 1

    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]

        if 0 > nr or nr >= M or 0 > nc or nc >= N:
            continue

        if arr[nr][nc] == 0 and not visited[nr][nc]:
            cnt += 1
            dfs(nr, nc)

    return cnt


M, N, K = map(int, input().split())
arr = [[0] * N for _ in range(M)]
for _ in range(K):
    r1, c1, r2, c2 = map(int, input().rstrip().split())
    nr1, nc1, nr2, nc2 = M-c2, r1, M-c1-1, r2-1
    for r in range(nr1, nr2+1):
        for c in range(nc1, nc2+1):
            arr[r][c] = 1

result = []
visited = [[0] * N for _ in range(M)]
for r in range(M):
    for c in range(N):
        if arr[r][c] == 0 and not visited[r][c]:
            cnt = 1
            answer = dfs(r, c)
            result.append(answer)

print(len(result))
for k in sorted(result):
    print(k, end=' ')