def solution(nums):
    N = max(nums)
    nums_cnt = [0] * (N + 1)
    for num in nums:
        nums_cnt[num] += 1
        
    count = 0
    for idx in nums_cnt:
        if idx != 0:
            count += 1
            
    if len(nums) // 2 < count:
        answer = len(nums) // 2
    else:
        answer = count
        
    return answer