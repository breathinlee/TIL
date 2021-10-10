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