from collections import deque
import sys

F, S, G, U, D = map(int, sys.stdin.readline().split())

visited = [0] * (F+1)
queue = deque([(S, 0)])
visited[S] = 1
ans = -1

while queue:
    position, cnt = queue.popleft()

    if position == G:
        ans = cnt
        break

    if position + U <= F and not visited[position + U]:
        visited[position + U] = 1
        queue.append(((position + U), cnt + 1))

    if position > D and not visited[position - D]:
        visited[position - D] = 1
        queue.append(((position - D), cnt + 1))

if ans == -1:
    print('use the stairs')
else:
    print(ans)