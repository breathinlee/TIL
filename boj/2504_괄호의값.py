# 1

import sys

def is_correct(chars):
    stack = []
    for char in chars:
        if char == '(' or char == '[':
            stack.append(char)
        elif stack and char == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(char)
        elif stack and char == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                stack.append(char)
        else:
            stack.append(char)

    if stack:
        return False
    return True


characters = sys.stdin.readline().strip()
stack = []

if is_correct(characters):
    for character in characters:
        if character == '(' or character == '[':
            stack.append(character)
        elif character == ')':
            result = 0
            if stack[-1] == '(':
                stack[-1] = 2
            else:
                for s in range(len(stack) - 1, -1, -1):
                    if stack[s] == '(':
                        stack[-1] = result * 2
                        break
                    else:
                        result += stack[s]
                        stack.pop()

        elif character == ']':
            result = 0
            if stack[-1] == '[':
                stack[-1] = 3
            else:
                for s in range(len(stack) - 1, -1, -1):
                    if stack[s] == '[':
                        stack[-1] = result * 3
                        break
                    else:
                        result += stack[s]
                        stack.pop()
    print(sum(stack))

else:
    print(0)



# 2

bracket = list(input())

stack = []
answer = 0
tmp = 1

for i in range(len(bracket)):

    if bracket[i] == "(":
        stack.append(bracket[i])
        tmp *= 2

    elif bracket[i] == "[":
        stack.append(bracket[i])
        tmp *= 3

    elif bracket[i] == ")":
        if not stack or stack[-1] == "[":
            answer = 0
            break
        if bracket[i-1] == "(":
            answer += tmp          
        stack.pop()
        tmp //= 2                   

    elif bracket[i] == "]":
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if bracket[i-1] == "[":
            answer += tmp           
        stack.pop()
        tmp //= 3                   

if stack:
    print(0)
else:
    print(answer)