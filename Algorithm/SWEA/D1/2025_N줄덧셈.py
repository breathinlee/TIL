"""
1부터 주어진 숫자만큼 모두 더한 값을 출
"""

n = int(input())

total = 0
for num in range(n+1):
    total += num
    num += 1
print(total) 