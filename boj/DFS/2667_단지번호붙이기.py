dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def dfs(r, c):
    global result

    visited[r][c] = 1

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]

        if 0 <= nr < N and 0 <= nc < N:
            if arr[nr][nc] and not visited[nr][nc]:
                result += 1
                dfs(nr, nc)

    return result


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]
cnt = 0
home = []

for r in range(N):
    for c in range(N):
        if arr[r][c] and not visited[r][c]:
            result = 1
            dfs(r, c)
            home.append(result)
            cnt += 1

print(cnt)
home.sort()
for h in home:
    print(h)