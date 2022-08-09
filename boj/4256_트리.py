import sys
input = sys.stdin.readline

def to_post(preorder, inorder):
    if preorder:
        parent = preorder[0]
        mid = inorder.index(parent)
        to_post(preorder[1:mid + 1], inorder[:mid])
        to_post(preorder[mid + 1:], inorder[mid + 1:])
        print(parent, end=" ")


T = int(input())
for _ in range(T):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    to_post(preorder, inorder)
    print()