def solution(s):
    answer = []
    start = ''
    s = s[2:-2].split('},{')
    s.sort(key=lambda x: len(x))
    
    for k in s:
        k = k.split(',')
        for t in k:
            if int(t) not in answer:
                answer.append(int(t))
    
    return answer