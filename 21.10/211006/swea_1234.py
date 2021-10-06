for tc in range(1, 11):
    N, numbers = input().split()
    N = int(N)
    numbers = list(numbers)
    i = 0

    while i < len(numbers)-1:
        if numbers[i:i+2] == numbers[i:i+2][::-1]:
            del numbers[i:i+2]
            i = 0
        else:
            i += 1

    print('#{} {}'.format(tc, ''.join(numbers)))