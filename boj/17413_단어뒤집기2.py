S = input()
answer = []
tmp = []
flag = False

if '<' in S:
    for char in S:
        if flag == True:
            tmp.append(char)
            if char == '>':
                flag = False
                answer += tmp
                tmp = []

        elif flag == False:
            if char == '<':
                answer += tmp[::-1]
                tmp = []
                tmp.append(char)
                flag = True

            elif char == ' ':
                answer += tmp[::-1]
                answer.append(char)
                tmp = []

            else:
                tmp.append(char)

    if tmp:
        answer += tmp[::-1]

    print(''.join(answer))

else:
    for word in S.split():
        tmp.append(word[::-1])

    answer = ' '.join(tmp)
    print(answer)