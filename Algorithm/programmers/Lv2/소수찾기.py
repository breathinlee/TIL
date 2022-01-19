from itertools import permutations
import math

def is_prime(num):
    num_sqrt = int(math.sqrt(num))
    
    if num < 2:
        return False
    
    for i in range(2, num_sqrt+1):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    answer = []
    nums = []
    numbers = list(numbers)
    
    for n in range(1, len(numbers) + 1):
        cases = permutations([n for n in range(len(numbers))], n)
    
        for case in cases:
            result = ''

            for i in range(n):
                result += numbers[case[i]]

            if result not in nums:
                nums.append(result)
          
    nums = list(set(map(int, nums)))
    
    for num in nums:
        if is_prime(num):
            answer.append(num)
                
    return len(answer)