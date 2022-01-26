a, b = map(int, input().split())
divisor = []

for i in range(1, max(a, b)+1):
    if a % i == 0 and b % i == 0:
        divisor.append(i)

min_value = divisor[-1]
max_value = (a // min_value) * (b // min_value) * min_value

print(min_value)
print(max_value)