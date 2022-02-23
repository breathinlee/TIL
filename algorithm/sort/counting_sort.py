# 카운팅 정렬

def counting_sort(nums):
    cnt_nums = [0] * (max(nums) - min(nums) + 1)
    for num in nums:
        cnt_nums[num - min(nums)] += 1

    sorted_nums = []
    for idx in range(len(cnt_nums)):
        sorted_nums += [idx + min(nums)] * cnt_nums[idx]
    
    return sorted_nums


numbers = [0, 55, 22, 33, 2, 1, 1, 10, 26, 42]
print(counting_sort(numbers))