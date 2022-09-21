def solution(n):
    binary_n = bin(n)[2:]
    binary_one_cnt = bin(n)[2:].count('1')
    answer = n + 1
    
    while True:
        if bin(answer)[2:].count('1') == binary_one_cnt:
            return answer
        
        answer += 1