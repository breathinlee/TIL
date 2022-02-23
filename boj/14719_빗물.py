H, W = map(int, input().split())
block = list(map(int, input().split()))

total = 0

for i in range(1, W-1):
    left_height = max(block[:i])
    right_height = max(block[i+1:])
    height = min(left_height, right_height)
    if height > block[i]:
        total += height - block[i]

print(total)