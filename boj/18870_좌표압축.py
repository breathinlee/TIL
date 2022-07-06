# sol 1

import sys
input = sys.stdin.readline

def binary_search(target):
    start = 0
    end = len(sorted_arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if sorted_arr[mid] == target:
            return mid
        elif sorted_arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1


N = int(input())
arr = list(map(int, input().split()))
sorted_arr = sorted(set(arr))
for a in arr:
    print(binary_search(a), end=' ')



# sol 2

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
sorted_arr = sorted(set(arr))
dict_arr = {p: idx for idx, p in enumerate(sorted_arr)}

for a in arr:
    print(dict_arr[a], end=' ')