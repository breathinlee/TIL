T = int(input())
for tc in range(1, T+1):
    N = int(input())
    incomes = list(map(int, input().split()))
    avg_incomes = sum(incomes)/N
    cnt = 0

    for income in incomes:
        if income <= avg_incomes:
            cnt += 1

    print('#{} {}'.format(tc, cnt))