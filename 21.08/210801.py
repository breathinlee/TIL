# SWEA 2050
"""
알파벳으로 이루어진 문자열을 입력 받아 각 알파벳을 1부터 26까지의 숫자로 변환하여 출력하라.
"""

for c in input():
    print(ord(c)-64, end=' ')


# SWEA 2047
"""
신문의 헤드라인을 편집하기 위해, 주어지는 문자열의 알파벳 소문자를 모두 대문자로 바꾸는 프로그램을 개발 중이다.
입력으로 주어진 문장에 모든 소문자 알파벳을 찾아 대문자로 변환한 다음, 그 결과를 출력하는 프로그램을 작성하라.
"""

sentence = input()
print(sentence.upper())


# SWEA 2046
"""
주어진 숫자만큼 # 을 출력해보세요.
"""

n = int(input())
print("#" * n)


# SWEA 2043
"""
서랍의 비밀번호가 생각이 나지 않는다.
비밀번호 P는 000부터 999까지 번호 중의 하나이다.
주어지는 번호 K부터 1씩 증가하며 비밀번호를 확인해 볼 생각이다.
예를 들어 비밀번호 P가 123 이고 주어지는 번호 K가 100 일 때, 100부터 123까지 24번 확인하여 비밀번호를 맞출 수 있다.
P와 K가 주어지면 K부터 시작하여 몇 번 만에 P를 맞출 수 있는지 알아보자.
"""

n, m = map(int, input(). split())
print(n - m + 1)


# SWEA 2029
"""
2개의 수 a, b를 입력 받아, a를 b로 나눈 몫과 나머지를 출력하는 프로그램을 작성하라.
"""

n = int(input())

for num in range(1, n+1):
    a, b = map(int, input(). split())
    print("#" + str(num), a // b, a % b)


# SWEA 2027
"""
주어진 텍스트를 그대로 출력하세요.
"""

for i in range(5):
    for j in range(5):
        if i == j:
            print("#", end = '')
        else:
            print("+", end = '')
    print() # 줄바꿈


# SWEA 2025
"""
1부터 주어진 숫자만큼 모두 더한 값을 출
"""

n = int(input())

total = 0
for num in range(n+1):
    total += num
    num += 1
print(total) 


# SWEA 1938
"""
두 개의 자연수를 입력받아 사칙연산을 수행하는 프로그램을 작성하라.
"""

a, b = map(int, input(). split())
print(a + b, a - b, a * b, a // b, sep = '\n')


# SWEA 1933
"""
입력으로 1개의 정수 N 이 주어진다.
정수 N 의 약수를 오름차순으로 출력하는 프로그램을 작성하라.
"""

n = int(input())

for i in range(1, n+1):
    if n % i:
        continue
    else:
        print(i, end = ' ')


# SWEA 1936
"""
A와 B가 가위바위보를 하였다.
가위는 1, 바위는 2, 보는 3으로 표현되며 A와 B가 무엇을 냈는지 입력으로 주어진다.
A와 B중에 누가 이겼는지 판별해보자. 단, 비기는 경우는 없다.
"""

a, b = map(int, input(). split())

if (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
    print('B')
else:
    print('A')


# SWEA 2019
"""
1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.
"""

n = int(input())
for i in range(n+1):
    print(2 ** i, end = ' ')


# SWEA 1545
"""
주어진 숫자부터 0까지 순서대로 찍어보세요.
"""

n = int(input())
for i in range(n, -1, -1):
    print(i, end = ' ')