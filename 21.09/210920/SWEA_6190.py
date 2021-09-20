def is_monotonic_increasing(number):
    num = str(number)
    for n in range(len(num) - 1):
        if num[n] > num[n+1]:
            return 0
    return 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    max_val = -1
    for i in range(N-1):
        for j in range(i+1, N):
            my_sum = numbers[i] * numbers[j]
            if is_monotonic_increasing(my_sum):
                if max_val < my_sum:
                    max_val = my_sum

    print('#{} {}'.format(tc, max_val))