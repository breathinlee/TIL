def solution(progresses, speeds):
    answer = []
    queue = []
    for k in range(len(speeds)):
        days = (100 - progresses[k])
        if days % speeds[k]:
            queue.append(days // speeds[k] + 1)
        else:
            queue.append(days // speeds[k])

    result = 1
    tmp = queue.pop(0)
    while queue:
        ans = queue.pop(0)
        if tmp >= ans:
            result += 1
        else:
            answer.append(result)
            result = 1
            tmp = ans
            
    answer.append(result)
            
    return answer