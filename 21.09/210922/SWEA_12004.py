T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]

    for number in numbers:
        if N % number == 0:
            N //= number
            if N < 10:
                ans = 'Yes'
            else:
                ans = 'No'
            break
    else:
        ans = 'No'

    print('#{} {}'.format(tc, ans))