def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))     
    numbers = sorted(numbers, key = lambda x: x*3, reverse = True)
    for number in numbers:
        answer += number
    
    if answer == '0' * len(answer):
        answer = '0'
        
    return answer