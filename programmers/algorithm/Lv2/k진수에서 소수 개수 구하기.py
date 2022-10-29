import math

def convert_num(n, k):
    tmp = ''
    while n:
        tmp = str(n%k) + tmp
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
    answer = -1
    result = convert_num(int(str(n), 10), k)
    if '0' not in result and is_prime(int(result)):
        answer += 1

    else:
        tmp = ''
        start = 0

        for idx, r in enumerate(result):
            if r != '0':
                tmp += r
                if start != 0 and idx == len(result) - 1:
                    if is_prime(int(tmp)) and result[start - 1] == '0':
                        answer += 1
            else:
                if len(tmp) and is_prime(int(tmp)):
                    if start == 0:
                        answer += 1
                        start = idx + 1

                    else:
                        if result[start - 1] == '0':
                            answer += 1
                            start = idx + 1

                tmp = ''
                
    return answer + 1