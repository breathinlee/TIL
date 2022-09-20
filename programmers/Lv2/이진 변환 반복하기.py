def get_binary_num(n, change_cnt):
    tmp = ''
    change_cnt += 1
    while n:
        tmp = str(n % 2) + tmp
        n //= 2
    return tmp


def solution(s):
    answer = []
    zero_cnt = 0
    change_cnt = 0

    while True:
        if s == '1':
            break

        zero_cnt += s.count('0')
        s = get_binary_num(len(s.replace('0', '')), change_cnt)
        change_cnt += 1

    answer.append(change_cnt)
    answer.append(zero_cnt)

    return answer