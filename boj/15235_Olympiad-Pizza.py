from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
pizza = list(map(int, input().split()))

time = [0] * N
feed_time  = 0

queue = deque()

for k in range(N):
    queue.append([k, 0])

while queue:
    pizza_num, pizza_cnt = queue.popleft()

    feed_time += 1
    pizza_cnt += 1

    if pizza[pizza_num] == pizza_cnt:
        time[pizza_num] = feed_time

    else:
        queue.append([pizza_num, pizza_cnt])

print(*time)