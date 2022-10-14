import sys

while True:
    sentence = sys.stdin.readline().rstrip()
    stack = []

    if sentence == '.':
        break

    for s in sentence:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if len(stack) and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s)
                break
        elif s == ']':
            if len(stack) and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(s)
                break
        elif s == '.':
            break

    if len(stack):
        print('no')
    else:
        print('yes')