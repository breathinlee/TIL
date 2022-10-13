def checkParenthesis(str):
    stack = []

    for s in str:
        if s == '(':
            stack.append(s)
        else:
            if not stack:
                return False
            else:
                stack.pop()

    if stack:
        return False
    return True


T = int(input())
for _ in range(T):
    ps = input()
    print('YES') if checkParenthesis(ps) else print('NO')