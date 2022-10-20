import sys
input = sys.stdin.readline

N = int(input())
stack = []
operations = []
number = 1
flag = False

for _ in range(N):
    tmp = int(input())

    while number <= tmp:
        stack.append(number)
        operations.append('+')
        number += 1

    if stack[-1] == tmp:
        stack.pop()
        operations.append('-')

    else:
        flag = True

if flag:
    print('NO')
else:
    for oper in operations:
        print(oper)