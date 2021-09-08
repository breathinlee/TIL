# sol 1
T = int(input())
for tc in range(1, T+1):
    word = input()

    if word == word[::-1]:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))


# so1 2
T = int(input())
for tc in range(1, T+1):
    word = input()
    l = len(word)
    idx = 0

    while idx < l//2:
        if word[idx] == word[-idx-1]:
            ans = 1
            idx += 1
        else:
            ans = 0
            break

    print('#{} {}'.format(tc, ans))