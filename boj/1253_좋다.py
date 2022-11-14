import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
nums.sort()

result = 0

for k in range(N):
    target = nums[k]
    start, end = 0, N - 2
    numbers = nums[:k] + nums[k+1:]

    while start < end:
        target1, target2 = numbers[start], numbers[end]
        total = target1 + target2

        if total == target:
            result += 1
            break

        elif total < target:
            start += 1

        else:
            end -= 1

print(result)