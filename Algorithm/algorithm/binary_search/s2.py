# recursion

def binary_search(numbers, target, start, end):
    if start <= end:
        mid = start + (end - start) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] > target:
            return binary_search(numbers, target, start, mid - 1)
        else:
            return binary_search(numbers, target, mid + 1, end)
    else:
        return -1


numbers = [6, 2, 3, 4, 5, 30, 1, 85, 10, 15, 40]
numbers.sort()
target = 2  # 있으면, 해당 요소의 인덱스 반환

start = 0
end = len(numbers) - 1
find_value = binary_search(numbers, target, start, end)

if find_value == -1:
    print('{}(은)는 없습니다.'.format(target))
else:
    print('{}(은)는 {}번째에 있습니다.'.format(target, find_value))
