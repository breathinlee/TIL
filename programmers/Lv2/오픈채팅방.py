def solution(record):
    answer = []
    id_nickname = {}
    
    for r in record:
        r = r.split(' ')
        
        if len(r) > 2:
            id_nickname[r[1]] = r[2]
            
    for r in record:
        r = r.split(' ')
        name = id_nickname[r[1]]
        if r[0] == 'Enter':
            answer.append(name + '님이 들어왔습니다.')
        elif r[0] == 'Leave':
            answer.append(name + '님이 나갔습니다.')
        
    return answer