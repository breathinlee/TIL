from itertools import combinations
import math

def is_prime(num):
    num_sqrt = int(math.sqrt(num))
    
    if num_sqrt == 1:
        return False
    
    for i in range(2, num_sqrt+1):
        if num % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    
    cases = combinations(nums, 3)
    for case in cases:
        if is_prime(sum(case)):
            answer += 1
            
    return answer