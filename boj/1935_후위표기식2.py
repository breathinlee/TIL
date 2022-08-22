import sys
input = sys.stdin.readline

N = int(input())
expression = input().rstrip()
number = []
for k in range(N):
    number.append(int(input()))

stack = []

for k in range(len(expression)):
    if expression[k].isalpha():
        tmp = ord(expression[k]) - ord('A')
        stack.append(number[tmp])

    else:
        operator = expression[k]
        a, b = stack.pop(), stack.pop()
        if operator == '*':
            stack.append(b*a)
        elif operator == '+':
            stack.append(b+a)
        elif operator == '-':
            stack.append(b-a)
        else:
            stack.append(b/a)

print(format(stack[0], ".2f"))
