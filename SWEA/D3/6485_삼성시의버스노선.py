T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bus_stop = [0] * 5001
    for _ in range(N):
        A, B = map(int, input().split())
        for k in range(A, B+1):
            bus_stop[k] += 1

    P = int(input())
    result = []
    for _ in range(P):
        stop = int(input())
        result.append(bus_stop[stop])

    print('#{}'.format(tc), end=' ')
    print(*result)