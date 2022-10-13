import sys
input = sys.stdin.readline

def calculate(num):
    total = 0
    for tree in trees:
        if tree > num:
            total += (tree - num)

    return total


N, M = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 0, max(trees)

while start <= end:
    mid = (start + end) // 2

    if calculate(mid) < M:
        end = mid - 1

    else:
        start = mid + 1

print(end)