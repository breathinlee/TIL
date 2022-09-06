import sys
input = sys.stdin.readline

def find(x):
    if friend[x] != x:
        friend[x] = find(friend[x])
    return friend[x]


def union(a, b):
    a, b = find(a), find(b)
    friend[b] = a


n = int(input())
m = int(input())
friend = [i for i in range(n+1)]
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

print(len(set(friend))-1)
