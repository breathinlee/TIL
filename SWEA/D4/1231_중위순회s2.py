def in_order(node):
    if tree[node][1]:
        in_order(tree[node][1])
    print(tree[node][0], end='')
    if tree[node][2]:
        in_order(tree[node][2])


for tc in range(1, 11):
    N = int(input())
    node_info = [list(input().split()) for _ in range(N)]   # tc, 해당 정점의 알파벳, 해당 정점의 왼쪽 자식, 오른쪽 자식의 정점번호
    tree = [[0] * 3 for _ in range(N+1)]

    for k in range(N):
        tree[int(node_info[k][0])][0] = node_info[k][1]
        if len(node_info[k]) == 2:
            pass
        elif len(node_info[k]) == 3:
            tree[int(node_info[k][0])][1] = int(node_info[k][2])
        else:
            tree[int(node_info[k][0])][1] = int(node_info[k][2])
            tree[int(node_info[k][0])][2] = int(node_info[k][3])


    print('#{}'.format(tc), end=' ')
    in_order(1)
    print()