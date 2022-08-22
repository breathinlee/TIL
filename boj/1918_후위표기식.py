import sys

expression = sys.stdin.readline()
stack = []
result = ''

for e in expression:
    if e.isalpha():
        result += e
    elif e == '(':
        stack.append(e)
    elif e == ')':
        while stack and stack[-1] != '(':
            tmp = stack.pop()
            result += tmp
        stack.pop()
    elif e == '+' or e == '-':
        while stack and stack[-1] != '(':
            tmp = stack.pop()
            result += tmp
        stack.append(e)
    elif e == '*' or e == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            tmp = stack.pop()
            result += tmp
        stack.append(e)

while stack:
    result += stack.pop()

print(result)