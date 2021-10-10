T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    numbers.sort()
    total = 0

    for k in range(1, 9):
        total += numbers[k]
        mean = round(total / 8, 0)

    print('#{} {}'.format(tc, int(mean)))