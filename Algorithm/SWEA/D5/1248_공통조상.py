def search_parents(node):
    p = []
    while True:
        node_parent = tree[node][2]
        if node_parent == 0:
            break
        p.append(node_parent)
        node = node_parent
    return p


def find_size(node):
    global cnt

    if node:
        cnt += 1
        find_size(tree[node][0])
        find_size(tree[node][1])


T = int(input())
for tc in range(1, T+1):
    V, E, node1, node2 = map(int, input().split())
    data = list(map(int, input().split()))

    tree = [[0] * 3 for _ in range(V+1)]
    for k in range(E):
        parent, child = data[2*k], data[2*k+1]
        if tree[parent][0]:
            tree[parent][1] = child
        else:
            tree[parent][0] = child
        tree[child][2] = parent

    node1_p = search_parents(node1)
    node2_p = search_parents(node2)
    cnt = 0

    for node in node1_p:
        if node in node2_p:
            common_root = node
            break

    find_size(common_root)

    print('#{} {} {}'.format(tc, common_root, cnt))