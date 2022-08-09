import sys
input = sys.stdin.readline

def count_sum(cnt, arr, dp):
    for k in range(cnt):
        ret = 0
        for s in range(k, k+cnt):
            ret += arr[s % cnt]
            if ret <= size:
                dp[ret] += 1
            else:
                break

    if sum(arr) <= size:
        dp[sum(arr)] = 1


size = int(input())
A, B = map(int, input().split())
A_pizza = [int(input()) for _ in range(A)]
B_pizza = [int(input()) for _ in range(B)]

total = 0
A_dp, B_dp = [0] * (size+1), [0] * (size+1)

count_sum(A, A_pizza, A_dp)
count_sum(B, B_pizza, B_dp)

for k in range(1, size):
    total += A_dp[k] * B_dp[size - k]

total += A_dp[size] + B_dp[size]

print(total)