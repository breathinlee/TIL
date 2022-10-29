def solution(dartResult):
    number = 0
    stack = []
    calculation = {'S': 1, 'D': 2, 'T': 3}
    flag = False

    for k in range(len(dartResult)):
        if dartResult[k].isalpha():
            number = number ** calculation[dartResult[k]]
            stack.append(number)
            flag = False
        elif dartResult[k] == '*':
            if len(stack) > 1:
                a = stack.pop()
                b = stack.pop()
                stack.append(b*2)
                stack.append(a*2)
            else:
                a = stack.pop()
                stack.append(a*2)
        elif dartResult[k] == '#':
            a = stack.pop()
            stack.append(a*(-1))
        else:
            if flag:
                number = int(dartResult[k-1] + dartResult[k])
            else:
                number = int(dartResult[k])
                flag = True

    return sum(stack)