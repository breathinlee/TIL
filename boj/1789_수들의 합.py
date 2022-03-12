import sys
import math

S = int(sys.stdin.readline())
k = int(math.sqrt(S*2))
ret = 0
cnt = 0
for i in range(1, k+2):
    ret += i
    cnt += 1
    if ret > S:
        break

print(cnt-1)
