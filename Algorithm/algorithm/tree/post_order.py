# 후위 순회 : 자식노드를 좌우 순서로 방문한 후, 부모노드로 방문
# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

def post_order(node):
    if node != 0:
        post_order(tree[node][0])          # 왼쪽
        post_order(tree[node][1])          # 오른쪽
        print('{}'.format(node), end=' ')


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

print('후위 순회: ', end=' ')
post_order(1)

# 후위 순회:  12 7 4 2 8 9 5 10 13 11 6 3 1 

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