import math

def is_prime(n):
    if n == 1:
        return False
    else:
        n_sqrt = int(math.sqrt(n))
        for k in range(2, n_sqrt+1):
            if n % k == 0:
                return False
        return True


def solution(n):
    answer = 0
    for num in range(1, n+1):
        if is_prime(num):
            answer += 1
    return answer