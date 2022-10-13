# sol 1 (284ms / 38648KB)
from collections import deque
import sys
input = sys.stdin.readline

d = [1, -1, 2]

def bfs(start):
    queue = deque([start])
    visited[start] = 1

    while queue:
        position = queue.popleft()

        if position == K:
            return visited[K] - 1

        for k in range(3):
            if k == 2:
                next_position = position * d[k]
            else:
                next_position = position + d[k]

            if next_position < 0 or next_position >= (2*size):
                continue

            if not visited[next_position]:
                visited[next_position] = visited[position] + 1
                queue.append(next_position)

    return visited[K] - 1


N, K = map(int, input().split())
size = max(N, K)
visited = [0] * (2*size)  # 이렇게 할 경우 최댓값 100,000이 나왔을 때 200,000크기의 배열이 만들어지기 때문에 더 비효율적
if N == K:
    print(0)
else:
    print(bfs(N))


# sol 2 (148ms / 34692KB)
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    queue = deque([N])

    while queue:
        position = queue.popleft()

        if position == K:
            return dist[K]

        for next_position in (position - 1, position + 1, position * 2):
            if next_position < 0 or next_position >= 100001:
                continue

            if not dist[next_position]:
                dist[next_position] = dist[position] + 1
                queue.append(next_position)


N, K = map(int, input().split())
dist = [0] * 100001
print(bfs())