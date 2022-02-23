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