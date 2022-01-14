def solution(priorities, location):
    answer = 0
    p_list = []
    
    # queue = []
    # for idx, p in enumerate(priorities):
    #     queue.append((idx, p))

    queue =  [(i,p) for i,p in enumerate(priorities)]
    
    docu = queue[location]    
    
    while queue:
        j = queue.pop(0)
        
        for q in queue:
            if j[1] < q[1]:
                queue.append(j)
                break
        else:
            p_list.append(j)
    
    for t in range(len(p_list)):
        if p_list[t] == docu:
            answer = t+1
        
    return answer