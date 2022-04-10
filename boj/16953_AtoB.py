import sys

input = sys.stdin.readline

A, B = map(int, input().split())
answer = 1

queue = [A]

while True:
    next = []
    for q in queue:
        if q > B:
            continue
        next.append(q * 2)
        next.append(int(str(q) + '1'))

    if len(queue) == 0:
        answer = -1
        break

    answer += 1

    if B in next:
        break
    queue = next

print(answer)