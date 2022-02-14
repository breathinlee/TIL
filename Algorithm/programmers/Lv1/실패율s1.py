def solution(N, stages):
    answer = []
    result = [0] * N
    stage_cnt = [0] * (N+1)
    stop_stage = [0] * (N+1)
    
    for k in range(1, N+1):
        for s in stages:
            if s >= k:
                stage_cnt[k] += 1
            if s == k:
                stop_stage[k] += 1
                
    for i in range(1, N+1):
        if stage_cnt[i] == 0:
            answer.append((i, 0))
        else:
            answer.append((i, stop_stage[i] / stage_cnt[i]))
        
    answer.sort(key=lambda x: -x[1])
    
    for a in range(N):
        result[a] = answer[a][0]
        
    return result