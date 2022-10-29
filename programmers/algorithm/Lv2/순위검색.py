from itertools import combinations
from collections import defaultdict

def solution(info, query):
    answer = []
    
    info_dict = defaultdict(list)
    
    for i in info:
        i = i.split()
        conditions = i[:-1]
        score = int(i[-1])
        
        for j in range(5):
            for case in combinations(conditions, j):
                case_condition = ''.join(case)
                info_dict[case_condition].append(score)
    
    for k in info_dict:
        info_dict[k].sort()
        
    for q in query:
        q = q.split(' ')
        q_condition = q[:-1]
        q_score = int(q[-1])
        
        for _ in range(3):
            q_condition.remove('and')
            
        while '-' in q_condition:
            q_condition.remove('-')
                
        q_condition = ''.join(q_condition)

        if q_condition in info_dict:
            i_scores = info_dict[q_condition]
            
            if len(i_scores):
                start, end = 0, len(i_scores)
                
                while start < end:
                    mid = (start + end) // 2
                    
                    if i_scores[mid] >= q_score:
                        end = mid
                    else:
                        start = mid + 1
                        
                answer.append(len(i_scores) - start)
                
        else:
            answer.append(0)
                
    return answer