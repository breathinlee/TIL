# 백준 11650

# import sys

# N = int(sys.stdin.readline())
# list = []
# for i in range(N):
#     x, y = map(int, sys.stdin.readline(). split())
#     list.append([x, y])
# list.sort()
# for data in list:    
#     print(data[0], data[1])

# input()쓰면 시간초과 나와서 sys.stdin.readline()으로 대체

# 백준 1015
"""
N = int(input())
numbers = list(map(int, input().split()))
idx_list = []
sorted_numbers = sorted(numbers)
for i in numbers:
    idx_list.append(sorted_numbers.index(i))
print(idx_list)
"""
# 이렇게 하면 리스트에서 같은 값이 들어있을 때 제대로 된 인덱스 출력 불가,,,

N = int(input())
numbers = list(map(int, input().split()))
c_numbers = numbers.copy()
c_numbers.sort()
idx_list = []
for i in numbers:
    cnt = 0
    # idx_list.append(c_numbers.index(i) + cnt)
    while numbers[-1]:
        if c_numbers.index(i) + cnt in idx_list:
            cnt += 1
        else:
            break
    idx_list.append(c_numbers.index(i) + cnt)
print(*idx_list)   

 

