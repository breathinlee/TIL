# 출발점 0 / 도착점 99 고정
# 각 정점의 길의 개수 최대 2개
# 길이 있으면 1 없으면 0

def dfs(node):
    visited[node] = 1

    for w in adj_list[node]:
        if not visited[w]:
            dfs(w)


for _ in range(1, 11):
    tc, E = map(int, input().split())
    tmp = list(map(int, input().split()))
    adj_list = [[] for _ in range(100)]         
    for i in range(E):
        adj_list[tmp[2*i]].append(tmp[2*i+1])
    visited = [0] * 100
    dfs(0)

    if visited[99] == 1:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))