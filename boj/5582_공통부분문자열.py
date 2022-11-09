# pypy3로 통과 (dp이용)

import sys
input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()
A_length = len(A)
B_length = len(B)
A = ' ' + A
B = ' ' + B
dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
total = 0

for k in range(1, A_length + 1):
    for s in range(1, B_length + 1):
        if A[k] == B[s]:
            dp[k][s] = dp[k-1][s-1] + 1
            total = max(dp[k][s], total)
print(total)


# python3로 통과

import sys
input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()

start, end = 0, 1
total = 0

# 이렇게 하면 index out of range 발생 x 
if len(A) > len(B):
    A, B = B, A

while start <= end and end <= len(A):
    sliced_string = A[start:end]
    if sliced_string not in B:
        start += 1
    else:
        total = max(total, len(sliced_string))

    end += 1

print(total)