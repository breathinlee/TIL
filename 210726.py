# 2072
'''
10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.
'''
T = int(input())

def odd_sums(lst):
    for i in lst:
        if i % 2:
            return sum(i)

result = 0
for _ in range(T):
    for data in list(map(int, input(). split())):
        print(odd_sums()) 

for data in range(1, T+1):
    numbers = map(int, input(). split())
    result = 0
    for num in numbers:
        if num % 2 != 0:
            result += num
    print('#' + str(data), result)


# 2071
'''
10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.
(소수점 첫째 자리에서 반올림한 정수를 출력한다.)
'''
T = int(input())

for data in range(1, T+1):
    numbers = list(map(int, input(). split()))
    print('#' + str(data), round(sum(numbers)/10))
