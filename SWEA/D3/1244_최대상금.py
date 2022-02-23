def swap(s, numpad):
    global cnt, ans

    if cnt == exchange:
        ans = max(ans, int(''.join(numpad)))
        return
    else:
        for i in range(s, len(numpad)-1):
            for j in range(i+1, len(numpad)):
                if numpad[i] <= numpad[j]:
                    numpad[i], numpad[j] = numpad[j], numpad[i]
                    cnt += 1
                    swap(i, numpad)
                    numpad[i], numpad[j] = numpad[j], numpad[i]
                    cnt -= 1


numpad, exchange = input().split()
exchange = int(exchange)
numpad = list(numpad)
cnt = 0
ans = 0

swap(0, numpad)

if ans == 0:
    left_exchange = exchange - cnt
    if left_exchange % 2:
        numpad[-2], numpad[-1] = numpad[-1], numpad[-2]
    ans = int(''.join(numpad))


print('{}'.format(ans))