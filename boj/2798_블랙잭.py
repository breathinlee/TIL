N, M = map(int, input().split())
numbers = list(map(int, input().split()))
cnt = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            tmp = numbers[i] + numbers[j] + numbers[k]
            if tmp > M:
                continue
            else:
                cnt = max(cnt, tmp)

print(cnt)