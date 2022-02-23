months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']

def solution(a, b):
    answer = ''
    day = 0
    
    for k in range(a-1):
        day += months[k]

    day += b-1
    answer += days[day % 7]

    return answer