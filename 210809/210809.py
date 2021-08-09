# 11151.03_배열1_이웃원소의합
"""
N 개의 정수값들이 주어질 때, 인접한 두 원소의 합이 최대인 경우를 찾으시오.
인접한 두 원소는 입력으로 주어지는 순서가 연속적인 2개의 값을 의미한다.
"""

N = int(input())
for k in range(N):
    numbers = int(input())
    data = list(map(int, input(). split()))
    max_data = data[0] + data[1]
    for i in range(numbers-2):
        if max_data < data[i+1] + data[i+2]:
            max_data = data[i+1] + data[i+2]
            i += 1
        else:
            continue
    print('#' + str(k+1), max_data)



# 1966. 숫자를 정렬하자 
"""
주어진 N 길이의 숫자열을 오름차순으로 정렬하여 출력하라.
"""

N = int(input())
for k in range(N):
    numbers = int(input())
    data = list(map(int, input(). split()))
    for j in range(numbers - 1, 0, -1):
        for i in range(0, j):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
    print('#' + str(k+1), *data)