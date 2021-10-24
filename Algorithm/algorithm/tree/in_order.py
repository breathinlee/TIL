# 중위 순회 : 왼쪽 자식노드, 부모노드, 오른쪽 자식노드 순으로 방문
# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

def in_order(node):
    if node != 0:
        in_order(tree[node][0])          # 왼쪽
        print('{}'.format(node), end=' ')
        in_order(tree[node][1])          # 오른쪽


V = int(input())
E = V - 1
temp = list(map(int, input().split()))
tree = [[0] * 3 for _ in range(V+1)]     # 왼쪽 자식, 오른쪽 자식, 부모노드
for i in range(E):
    parent, child = temp[i*2], temp[i*2+1]
    if not tree[parent][0]:
        tree[parent][0] = child
    else:
        tree[parent][1] = child
    tree[child][2] = parent

print('중위 순회: ', end=' ')
in_order(1)

# 중위 순회:  12 7 4 2 1 8 5 9 3 10 6 13 11

"""
               1
             /   \
            2     3
           /     /  \
          4     5    6
         /     / \  / \
        7     8  9 10  11
       /               /
     12              13
"""