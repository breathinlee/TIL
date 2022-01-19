# sol 1
def solution(answers):
    answer = []
    result = []
    people1 = [1, 2, 3, 4, 5]
    people2 = [2, 1, 2, 3, 2, 4, 2, 5]
    people3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    idx = 0
    cnt_1 = 0
    cnt_2 = 0
    cnt_3 = 0
    
    while idx < len(answers):
        if answers[idx] == people1[idx % 5]:
            cnt_1 += 1
        if answers[idx] == people2[idx % 8]:
            cnt_2 += 1
        if answers[idx] == people3[idx % 10]:
            cnt_3 += 1
            
        idx += 1
    
    result.append((1, cnt_1))
    result.append((2, cnt_2))
    result.append((3, cnt_3))
    
    result.sort(key = lambda  x :(-x[1], x[0]))
    
    for r in range(len(result) - 1):
        if result[r][1] != result[r+1][1]:
            answer.append(result[r][0])
            break
        else:
            answer.append(result[r][0])
            if r == 1:
                answer.append(result[2][0])
        
    return answer


# sol 2
def solution(answers):
    pattern = [[1, 2, 3, 4, 5],
                [2, 1, 2, 3, 2, 4, 2, 5],
                [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern[0][idx % 5]:
            score[0] += 1
        if answer == pattern[1][idx % 8]:
            score[1] += 1
        if answer == pattern[2][idx % 10]:
            score[2] += 1
        
    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx + 1)

    return result
