# 최빈값 구할 때 collections 모듈의 Counter 클래스 사용
# 가장 많이 나온 데이터나 가장 적게 나온 데이터 찾을 때 유용
# most_common() 메서드는 데이터의 개수가 많은 순으로 정렬된 배열 리턴 !!!

from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort()
print(round(sum(nums) / N))
print(nums[N//2])
if len(nums) > 1:
    nums_list = Counter(nums).most_common()
    max_idx, max_value = nums_list[0]
    sec_idx, sec_value = nums_list[1]
    if max_value == sec_value:
        print(sec_idx)
    else:
        print(max_idx)
else:
    print(nums[0])

print(nums[-1] - nums[0])