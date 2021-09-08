# 백준 2577번 숫자의 개수
"""
세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
"""

a = int(input())
b = int(input())
c = int(input())
product = str(a*b*c)

for number in range(10):
   number_count = product.count(str(number))
   print(number_count) 


# 백준 2750번 수 정렬하기
"""
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
"""

n = int(input())
numlist = []

for i in range(n):
    numlist.append(int(input()))
    
new_numlist = sorted(numlist)
for k in new_numlist:
    print(k)
