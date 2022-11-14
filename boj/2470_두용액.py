# 투포인터 문제

import sys
input = sys.stdin.readline

N = int(input())
solution = list(map(int, input().split()))
solution.sort()

start, end = 0, N-1
result = 2e9
answer = []

while start < end:
    sol1 = solution[start]
    sol2 = solution[end]

    sum_sols = sol1 + sol2

    if abs(sum_sols) < result:
        result = abs(sum_sols)
        answer = [sol1, sol2]

    if sum_sols < 0:
        start += 1

    else:
        end -= 1

print(answer[0], answer[1])