from itertools import permutations

def calculate(arr):
    first = arr.pop(0)
    while arr:
        o = arr.pop(0)
        n = arr.pop(0)

        if o == '+':
            first += n
        elif o == '-':
            first -= n
        elif o == '*':
            first *= n
        else:
            if first < 0:
                first = -((-first) // n)
            else:
                first = first // n

    return first


N = int(input())
num = list(map(int, input().split()))
cnt = list(map(int, input().split()))
temp = ['+', '-', '*', '/']
min_value = 987654321
max_value = -987654321

operator = []
idx = 0
while idx < 4:
    if cnt[idx] == 0:
        pass
    else:
        for _ in range(cnt[idx]):
            operator.append(temp[idx])
    idx += 1

cases = list(set(permutations(operator, len(operator))))
for case in cases:
    idx = 0
    stack = []
    while idx < len(case):
        stack.append(num[idx])
        stack.append(case[idx])
        idx += 1
    stack.append(num[-1])
    result = calculate(stack)

    if result < min_value:
        min_value = result

    if result > max_value:
        max_value = result

print(max_value)
print(min_value)