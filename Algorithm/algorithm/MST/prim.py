# 프림
#  - 정점 중심 (임의의 정점을 잡고 시작)
#  - 정점과 인접하는 정점 중에서 최소 비용의 간선이 존재하는 정점 선택
#  - 계속 가중치가 최소인 정점을 연결해가며 최종적으로 연결된 배열의 합


# 첫 째 줄에 마지막 노드 번호 V와 간선의 개수 E
# 다음 줄부터 간선의 양 끝 노드(start, end)와 가중치(w)

# 4 6
# 0 1 10
# 0 2 7
# 1 4 2
# 2 3 10
# 2 4 3
# 3 4 10

def prim():
    for _ in range(V):
        min_idx = -1
        min_value = 987654321
        
        for i in range(V+1):
            if not visited[i] and key[i] < min_value:       # i번째 정점을 선택하지 않았고 선택하지 않은 정점 중에서 가장 적은 값이라면
                min_idx = i
                min_value = key[i]
        visited[min_idx] = 1

        for i in range(V+1):                                # min_idx와 연결된 인접 행렬 돌면서
            if not visited[i] and G[min_idx][i] < key[i]:   # 정점 선택 안했고 해당 가중치가 key의 요소보다 작으면 (== 더 적은 비용으로 MST에 연결되면)
                key[i] = G[min_idx][i]

    return sum(key)                                         # 최종 간선의 가중치


V, E = map(int, input().split())
G = [[987654321] * (V+1) for _ in range(V+1)]
key = [987654321] * (V+1)
key[0] = 0                                                  # 시작지점 => 가중치 0
visited = [0] * (V+1)
for i in range(E):
    start, end, W = map(int, input().split())
    G[start][end] = W
    G[end][start] = W

print(prim())