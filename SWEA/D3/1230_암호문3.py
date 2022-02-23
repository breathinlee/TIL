for tc in range(1, 11):
    N = int(input())
    password = list(map(int, input().split()))
    cnt = int(input())
    commands = list(input().split())
    idx = 0

    while idx < len(commands):
        if commands[idx] == 'I':
            x = int(commands[idx + 1])
            y = int(commands[idx + 2])
            s = commands[idx + 3:idx + 3 + y]
            password[x:x] = s
            idx += 3 + y
        elif commands[idx] == 'D':
            x = int(commands[idx + 1])
            y = int(commands[idx + 2])
            del password[x:x+y]
            idx += 1
        elif commands[idx] == 'A':
            x = int(commands[idx + 1])
            s = commands[idx + 2:idx + 2 + x]
            password.extend(s)
            idx += 2 + x
        else:
            idx += 1

    print('#{}'.format(tc), end=' ')
    for i in range(10):
        print(password[i], end=' ')
    print()