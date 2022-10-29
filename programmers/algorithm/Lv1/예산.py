def solution(d, budget):
    answer = 0
    d.sort()
    
    for v in range(len(d)):
        budget -= d[v]
        
        if budget < 0:
            answer = v
            break
            
    else:
        answer = len(d)
        
    return answer