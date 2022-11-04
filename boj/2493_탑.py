import sys
input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().rstrip().split()))
stack = []
sign = [0] * N

for k in range(N):
    while stack:
        if towers[stack[-1]] > towers[k]:
            sign[k] = stack[-1] + 1
            break
        else:
            stack.pop()
    stack.append(k)

print(' '.join(map(str, sign)))
