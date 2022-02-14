def solution(numbers):
    answer = []
    
    numbers.sort()
    
    for i in range(len(numbers) - 1):
        for j in range(i+1, len(numbers)):
            if (numbers[i] + numbers[j]) not in answer:
                answer.append(numbers[i] + numbers[j])
                
    return list(sorted(set(answer)))