def convertNumber(number, base):
    tmp = ''
    if number == 0:
        return '0'
    
    while number:
        remain = number % base
        if remain >= 10:
            remain = chr(ord('A') + remain - 10)
        tmp = str(remain) + tmp
        number //= base
        
    return tmp
    

def solution(n, t, m, p):
    answer = ''
    cnt = number = 0
    while cnt < t*m:
        tmp = convertNumber(number, n)
        answer += tmp
        number += 1
        cnt += len(tmp)
    
    result = ''
    idx = p-1
    
    while len(result) < t:
        result += answer[idx]
        idx += m    
        
    return result
