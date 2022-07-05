import math
import sys

def is_prime(num):
    if num == 1:
        return False

    num_sqrt = int(math.sqrt(num))
    for k in range(2, num_sqrt + 1):
        if num % k == 0:
            return False

    return True


N = int(input())
numbers = list(input().split())

cnt = 0

for number in numbers:
    if is_prime(int(number)):
        cnt += 1

print(cnt)