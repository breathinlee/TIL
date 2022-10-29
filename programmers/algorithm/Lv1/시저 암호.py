def solution(s, n):
    answer = ''
    for k in s:
        if k.isupper():
            temp = chr((ord(k) - ord('A') + n) % 26 + ord('A'))
            answer += temp
        elif k.islower():
            temp = chr((ord(k) - ord('a') + n) % 26 + ord('a'))
            answer += temp
        else:
            answer += k
    return answer