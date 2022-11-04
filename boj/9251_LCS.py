import sys
input = sys.stdin.readline

A = input().rstrip()  # ACAYKP
B = input().rstrip()  # CAPCAK

dp = [0] * len(A)

for b in range(len(B)):
    cnt = 0
    for a in range(len(A)):
        if A[a] == B[b]:
            dp[a] = cnt + 1
        elif cnt < dp[a]:
            cnt = dp[a]

print(max(dp))