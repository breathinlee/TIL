N = int(input())
picked_numbers = list(map(int, input().split()))   # 0 1 1 3 2
line_up = [1]
for i in range(2, N+1):
    line_up.insert(picked_numbers[i-1], i)
for j in range(N-1, -1, -1):
    print(line_up[j], end=' ')