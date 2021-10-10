def calculus(node):
    operator = ['+', '-', '*', '/']
    if tree[node][0] == operator[0]:
        return calculus(tree[node][1]) + calculus(tree[node][2])
    elif tree[node][0] == operator[1]:
        return calculus(tree[node][1]) - calculus(tree[node][2])
    elif tree[node][0] == operator[2]:
        return calculus(tree[node][1]) * calculus(tree[node][2])
    elif tree[node][0] == operator[3]:
        if calculus(tree[node][2]) == 0:
            return 0
        return calculus(tree[node][1]) / calculus(tree[node][2])
    else:
        return tree[node][0]


for tc in range(1, 11):
    N = int(input())
    tree = [[0] * 3 for _ in range(N + 1)]
    for i in range(N):
        temp = input().split()
        if len(temp) == 4:
            tree[i+1][0] = temp[1]
            tree[i+1][1] = int(temp[2])
            tree[i+1][2] = int(temp[3])
        else:
            tree[i+1][0] = int(temp[1])


    print('#{} {}'.format(tc, int(calculus(1))))