# 병합 정렬

def merge(left, right):
    if len(left) == 0:         # 왼쪽 배열 비어있으면 합칠 게 없으므로 오른쪽 반환
        return right
    if len(right) == 0:        # 오른쪽 배열 비어있으면 합칠 게 없으므로 왼쪽 반환
        return left
    sorted_list = []
    L = R = 0

    while len(sorted_list) != len(left) + len(right):
        if left[L] <= right[R]:
            sorted_list.append(left[L])
            L += 1
        else:
            sorted_list.append(right[R])
            R += 1
        
        if R == len(right):
            sorted_list += left[L:]
            break

        if L == len(left):
            sorted_list += right[R:]
            break

    return sorted_list


def partition(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    left = partition(nums[:mid])
    right = partition(nums[mid:])
    return merge(left, right)


numbers = [0, 55, 22, 33, 2, 1, 10, 26, 42]
print(partition(numbers))