N, K = map(int, input().split())
divisor = []

for n in range(1, N+1):
    if N % n == 0:
        divisor.append(n)
    if len(divisor) == K:
        answer = n
        break

else:
    answer = 0

print(answer)