T = int(input())
for tc in range(1, T+1):
    temp = input()
    a, b = 1, 1

    for i in range(len(temp)):
        if temp[i] == 'L':
            a, b = a, a+b
        else:
            a, b = a+b, b

    print('#{} {} {}'.format(tc, a, b))