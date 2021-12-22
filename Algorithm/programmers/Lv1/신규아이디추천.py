def solution(new_id):
    answer = ''
    
    # 1
    new_id = new_id.lower()
    
    # 2
    chars = ['-', '_', '.']
    for char in new_id:
        if char.isdigit() or char.isalpha() or char in chars:
            answer += char
    
    # 3
    while answer.count('..') >= 1:
        answer = answer.replace('..', '.')
        
    # 4
    answer = answer.strip('.')
    
    # 5
    if len(answer) == 0:
        answer = 'a'
    
    # 6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer.rstrip('.')
    
    # 7
    if len(answer) <= 2:
        answer += (answer[-1] * (3 - len(answer)))
        
    return answer