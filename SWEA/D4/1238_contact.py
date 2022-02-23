def bfs(node):
    queue = [node]
    visited[node] = 1

    while queue:
        start_node = queue.pop(0)
        for i in range(1, max(numbers)+1):
            if G[start_node][i] and not visited[i]:
                queue.append(i)
                visited[i] = 1
                cnt[i] = cnt[start_node] + 1


for tc in range(1, 11):
    l, start = map(int, input().split())
    numbers = list(map(int, input().split()))
    G = [[0] * (max(numbers)+1) for _ in range((max(numbers)+1))]
    for i in range(l//2):
        G[numbers[2*i]][numbers[2*i+1]] = 1

    visited = [0] * (max(numbers)+1)
    cnt = [0] * (max(numbers)+1)
    max_distance = 0

    bfs(start)

    for k in range(1, max(numbers)+1):
        if max_distance <= cnt[k]:
            max_distance = cnt[k]
            ans = k
    # if cnt.count(max_distance) > 1:
    #     ans = l - cnt[::-1].index(max_distance) - 1
    # else:
    #     ans = cnt.index(max_distance)

    print('#{} {}'.format(tc, ans))