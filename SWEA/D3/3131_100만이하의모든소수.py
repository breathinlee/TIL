N = 10 ** 6
numbers = [1] * (N+1)
numbers[0], numbers[1] = 0, 0

for i in range(2, N):
    if numbers[i]:
        for j in range(i*2, N, i):
            numbers[j] = 0

for i in range(N):
    if numbers[i]:
        print(i, end=' ')