T = int(input())
for tc in range(1, T+1):
    words = input()

    for i in range(3):
        a = words[i]
        if words.count(a) == 2:
            ans = 'Yes'
        else:
            ans = 'No'
            break

    print('#{} {}'.format(tc, ans))