def find_min_cost(G):
    global result

    idx = 0

    while idx < N:
        min_idx = -1
        min_value = float('inf')

        for i in range(N):
            if not visited[i] and key[i] < min_value:
                min_idx = i
                min_value = key[i]
        visited[min_idx] = 1
        idx += 1
        result += min_value

        for j in range(N):
            if not visited[j] and G[min_idx][j] < key[j]:
                key[j] = G[min_idx][j]


T = int(input())
for tc in range(1, T+1):
    N = int(input())       # 섬의 개수
    island_x = list(map(int, input().split()))
    island_y = list(map(int, input().split()))
    E = float(input())     # 환경 부담 세율

    G = [[0] * N for _ in range(N)]
    visited = [0] * N
    key = [float('inf')] * N
    key[0] = 0
    result = 0

    for i in range(N):
        for j in range(i+1, N):
            w = (island_x[i] - island_x[j]) ** 2 + (island_y[i] - island_y[j]) ** 2
            G[i][j] = w
            G[j][i] = w

    find_min_cost(G)
    print('#{} {}'.format(tc, round(result*E)))