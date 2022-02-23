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


