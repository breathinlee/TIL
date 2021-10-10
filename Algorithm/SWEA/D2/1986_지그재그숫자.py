T = int(input())
for tc in range(1, T+1):
    number = int(input())
    ret = 0

    for n in range(1, number+1):
        if n % 2:
            ret += n
        else:
            ret -= n

    print('#{} {}'.format(tc, ret))