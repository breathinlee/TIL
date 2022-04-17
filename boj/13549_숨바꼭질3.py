from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
visited = [0] * 100001

queue = deque([(N, 0)])
time = 0

while queue:
    now, tmp = queue.popleft()
    visited[now] = 1

    if now == K:
        time = tmp
        break

    if now + 1 < 100001 and not visited[now + 1]:
        queue.append((now + 1, tmp + 1))

    if now - 1 > -1 and not visited[now - 1]:
        queue.append((now - 1, tmp + 1))

    if now * 2 < 100001 and not visited[now * 2]:
        queue.appendleft((now * 2, tmp))

print(time)
