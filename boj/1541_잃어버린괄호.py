expression = input().split('-')
result = 0

for e in expression[0].split('+'):
    result += int(e)

for e in expression[1:]:
    for k in e.split('+'):
        result -= int(k)

print(result)