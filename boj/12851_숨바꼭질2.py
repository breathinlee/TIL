from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
visited = [0] * 100001

queue = deque([(N, 0)])
time = 0
cnt = 0
find_time = False

while queue:
    now, tmp = queue.popleft()
    visited[now] = 1

    if find_time and tmp > time:
        break

    if now == K:
        if not find_time:
            time = tmp
            find_time = True
        cnt += 1

    if now + 1 < 100001 and not visited[now + 1]:
        queue.append((now + 1, tmp + 1))

    if now - 1 > -1 and not visited[now - 1]:
        queue.append((now - 1, tmp + 1))

    if now * 2 < 100001 and not visited[now * 2]:
        queue.append((now * 2, tmp + 1))

print(time)
print(cnt)