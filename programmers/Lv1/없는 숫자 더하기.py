arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def solution(numbers):
    answer = 0
    
    for number in arr:
        if number not in numbers:
            answer += number
            
    return answer