T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = []
    idx = 1

    while len(numbers) < 10:
        number = N * idx
        while number > 0:
            if (number % 10) not in numbers:
                numbers.append(number % 10)
            number //= 10
            if len(numbers) == 10:
                ans = N * idx
                break
        idx += 1

    print('#{} {}'.format(tc, ans))