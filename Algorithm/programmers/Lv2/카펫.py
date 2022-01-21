import math

def solution(brown, yellow):
    answer = []
    num = int(math.sqrt(yellow))
    
    for i in range(1, num+1):
        if yellow % i:
            continue
        else:
            a = i
            b = yellow // i
            if (a+2)*(b+2) == brown + yellow:
                break
    
    answer.append(b+2)
    answer.append(a+2)
        
    return answer