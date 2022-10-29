def solution(n, words):
    answer = []
    turn = 1
    person = 2
    
    for k in range(1, len(words)):
        if words[k-1][-1] != words[k][0]:
            answer.append(person)
            answer.append(turn)
            break
        elif words[k] in words[:k]:
            answer.append(person)
            answer.append(turn)
            break
        
        person += 1
        
        if person == n+1:
            turn += 1
            person = 1
            
    else:
        answer.append(0)
        answer.append(0)
    
    return answer