T = int(input())
for tc in range(1, T+1):
    data = [list(input()) for _ in range(5)]
    result = []
    max_length = 0
    for i in range(5):
        length = len(data[i])
        if max_length < length:
            max_length = length
    for i in range(5):
        if len(data[i]) < max_length:
            difference = max_length - len(data[i])
            for j in range(difference):
                data[i].append('')

    for i in range(max_length):
        for j in range(5):
            result.append(data[j][i])
    ans = ''.join(result).split()
    print('#{} {}'.format(tc, *ans))