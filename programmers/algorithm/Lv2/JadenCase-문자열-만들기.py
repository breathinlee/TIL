def solution(s):
    s = s.split(' ')
    for k in range(len(s)):
        s[k] = s[k].capitalize()
    return ' '.join(s)