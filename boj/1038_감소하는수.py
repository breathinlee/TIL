import sys
from collections import deque

input = sys.stdin.readline

def find_number(N):
    queue = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
    cnt = 0

    while queue:
        start = queue.popleft()
        cnt += 1

        if cnt == N:
            return start

        end = int(str(start)[-1])
        for k in range(end):
            queue.append(int(str(start) + str(k)))

    return -1


N = int(input())
print(0) if N == 0 else print(find_number(N))