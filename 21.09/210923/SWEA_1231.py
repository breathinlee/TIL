def in_order(i):
    global ans
    if i <= N:
        in_order(i*2)
        ans += alphabet[i]
        in_order(i*2+1)

for tc in range(1, 11):
    N = int(input())
    alphabet = [0] * (N+1)
    ans = ''

    for k in range(N):
        temp = input().split()
        alphabet[k+1] = temp[1]

    in_order(1)

    print('#{} {}'.format(tc, ans))