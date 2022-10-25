from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    importance = deque(list(map(int, input().rstrip().split())))
    queue = deque([n for n in range(N)])
    cnt = 1

    while True:
        target = importance.popleft()
        docu = queue.popleft()

        for im in importance:
            if target < im:
                importance.append(target)
                queue.append(docu)
                break

        else:
            if M == docu:
                break

            else:
                cnt += 1

    print(cnt)