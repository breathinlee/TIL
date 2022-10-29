import math

def solution(left, right):
    answer = 0
    
    for num in range(left, right+1):
        cnt = 0
        num_sqrt = int(math.sqrt(num))
        for n in range(1, num_sqrt + 1):
            if n == num_sqrt:
                if n ** 2 == num:
                    cnt += 1
            else:
                if num % n == 0:
                    cnt += 2
        
        if cnt % 2:
            answer -= num
        else:
            answer += num
            
    return answer