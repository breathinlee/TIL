def solution(n):
    answer = ''
    numbers = [1, 2, 4]
    
    while n:
        n -= 1
        answer = str(numbers[n % 3]) + answer
        n //= 3
    
    return answer