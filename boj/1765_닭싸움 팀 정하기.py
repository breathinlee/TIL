import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a, b = find(a), find(b)
    parent[b] = a


n = int(input())
m = int(input())
parent = [i for i in range(n+1)]
enemy = [[] for _ in range(n+1)]
for _ in range(m):
    r, a, b = input().split()
    a, b = int(a), int(b)

    if r == 'F':
        union(a, b)

    else:
        if enemy[a]:
            for e in enemy[a]:
                union(e, b)

        if enemy[b]:
            for e in enemy[b]:
                union(e, a)

        enemy[a].append(b)
        enemy[b].append(a)

for i in range(1, n+1):
    find(i)

print(len(set(parent))-1)
