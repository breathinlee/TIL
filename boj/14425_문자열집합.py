'''
데이터를 빠르게 넣거나 가져올 때 
리스트 말고 해시(딕셔너리) 쓰자!! 
딕셔너리는 시간복잡도 O(1)이므로 아주 빠름..

**해시**
리스트를 쓸 수 없을 때(인덱스 값을 숫자가 아닌 문자열 혹은 튜플로 사용하려고 할 때)
빠른 접근 혹은 탐색이 필요할 때
집계가 필요할 때(collections모듈의 Counter와 함께 사용하면 아주 빠름)
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
hash = dict()
for _ in range(N):
    tmp = input()
    hash[tmp] = 1

result = 0

for _ in range(M):
    tmp = input()
    if tmp in hash:
        result += 1

print(result)