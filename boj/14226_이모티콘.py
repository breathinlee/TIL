import sys
from collections import deque

S = int(sys.stdin.readline())
dp = [[-1] * (S+1) for _ in range(S+1)]
dp[1][0] = 0
queue = deque([(1, 0)])

while queue:
    s, c = queue.popleft()

    if s <= 1000 and dp[s][s] == -1:
        dp[s][s] = dp[s][c] + 1
        queue.append((s, s))
    if s + c <= S and dp[s+c][c] == -1:
        dp[s+c][c] = dp[s][c] + 1
        queue.append((s+c, c))
    if s - 1 > -1 and dp[s-1][c] == -1:
        dp[s-1][c] = dp[s][c] + 1
        queue.append((s-1, c))

result = 987654321
for k in dp[S]:
    if k != -1:
        result = min(result, k)

print(result)
