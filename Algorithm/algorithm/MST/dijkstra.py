"""
0번 지점에서 V번 지점까지 이동하는데 걸리는 최소 거리 출력
방향 존재

첫 째 줄에 마지막 노드 번호 V(0번 부터 시작)와 간선의 개수 E
다음 줄부터 E개의 줄에 걸쳐 간선의 시작(start)과 끝(end) 그리고 구간의 거리(w) 정보

4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10

다익스트라
- 시작 지점으로부터 특정 지점까지의 최소 거리(비용)을 아는 것이 포인트
- 어떤 정점을 거쳐왔는지 알 수 없음
- prim과 비슷한 방식으로 구현
- 다만, 최소 비용을 갱신 하는 과정에서 차이가 발생
- 음수 가중치 허용하지 않음
"""

def dijkstra():
    for _ in range(V):
        min_idx = -1
        min_value = 987654321
        for i in range(V+1):
            if not visited[i] and min_value > dist[i]:
                min_idx = i
                min_value = dist[i]
    visited[min_idx] = 1
    
    for j in range(V+1):
        if not visited[j] and dist[j] > dist[min_idx] + G[min_idx][j]:   # 만약 j번 째를 방문하지 않았고 가려는 곳이 더 짧은 거리로 이동 가능하다면
            dist[j] = dist[min_idx] + G[min_idx][j]

    return dist[V]


V, E = map(int, input().split())                               # V: 마지막 노드 번호(0~V) / E: 간선
G = [[987654321 for _ in range(V+1)] for _ in range(V+1)]      # 가중치 초기화 (최소 거리를 구해야 하기 때문에 가중치로 사용하지 않는 큰 값으로 초기화)
dist = [987654321] * (V+1)                                     # 비용(거리) 초기화
dist[0] = 0                                                    # 시작 정점 지점 (0번 -> 0번의 거리는 0)
visited = [0] * (V+1)                                          # 방문 체크
for _ in range(E):
    start, end, w = map(int, input().split())                  # 유향(방향있는) 그래프
    G[start][end] = w                                          # 시작 / 끝 / 가중치(길이)
print(dijkstra())   