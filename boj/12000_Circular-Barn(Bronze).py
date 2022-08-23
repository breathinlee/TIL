import sys
input = sys.stdin.readline

N = int(input())
cows = []
for k in range(N):
    cows.append(int(input().rstrip()))

total = 987654321

for i in range(N):
    ret = 0
    for j in range(i, i+N):
        ret += (cows[j % N] * (j-i))

        if ret > total:
            break

    total = min(ret, total)

print(total)