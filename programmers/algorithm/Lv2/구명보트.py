def solution(people, limit):
    answer = 0
    people.sort()
    idx = 0 
    back_idx = -1
    while idx < len(people) and back_idx >= -len(people):
        if people[idx] + people[back_idx] > limit:
            answer += 1
            back_idx -= 1
        else:
            answer += 1
            idx +=1 
            back_idx -= 1
        if idx - back_idx > len(people): break
        
    return answer