# sol 1
def solution(n):
    answer = 0
    reverse_ternary = ''
    
    while n:
        n, mod = divmod(n, 3)
        reverse_ternary += str(mod)
    
    t = len(reverse_ternary)
    for k in range(t):
        answer += int(reverse_ternary[t-k-1]) * (3 ** k)
        
    return answer


# sol 2
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n //= 3

    answer = int(tmp, 3)
    return answer
