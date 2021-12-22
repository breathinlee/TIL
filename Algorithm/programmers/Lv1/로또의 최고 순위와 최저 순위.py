def solution(lottos, win_nums):
    winner = [10, 6, 5, 4, 3, 2]
    answer = []
    cnt = 0
    zero_cnt = lottos.count(0)
    for lotto in lottos:
        if lotto in win_nums:
            cnt += 1
    
    max_cnt = cnt + zero_cnt        
    
    if max_cnt != 0 and max_cnt in winner:
        answer.append(winner.index(max_cnt))
    else:
        answer.append(6)
        
    if cnt != 0 and cnt in winner:
        answer.append(winner.index(cnt))
    else:
        answer.append(6)
        
    return answer