def solution(n):
    answer = 0
    for k in range(1, n+1):
        total = n
        i = 0
        while total > 0:
            total -= (k+i)
            i += 1
            
        if total == 0:
            answer += 1 
    
    return answer