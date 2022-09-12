import math

def convert_num(n, k):
    tmp = ''
    while n:
        tmp = str(n % k) + tmp
        n //= k
    return tmp


def is_prime(number):
    math_sqrt = math.sqrt(number)

    if number == 1:
        return False

    else:
        for k in range(2, int(math_sqrt) + 1):
            if number % k == 0:
                return False

    return True


def solution(n, k):
    answer = 0
    result = convert_num(n, k)

    for num in result.split('0'):
        if not num:
            continue
        if is_prime(int(num)):
            answer += 1

    return answer
