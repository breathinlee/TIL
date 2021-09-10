T = int(input())
for tc in range(1, T+1):
    exchange = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    idx = 0
    count = []

    while idx < 8:
        count.append(exchange // money[idx])
        exchange = exchange % money[idx]
        idx += 1

    print('#{}'.format(tc))
    print(*count)
