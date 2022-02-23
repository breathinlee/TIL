# 버블 정렬

def bubble_sort(nums):
    for i in range(len(nums)-1, -0, -1):
        for j in range(i):
            if nums[j] > nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
            
    return nums


numbers = [0, 55, 22, 33, 2, 1, 1, 10, 26, 42]
print(bubble_sort(numbers))