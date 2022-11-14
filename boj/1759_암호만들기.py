from itertools import combinations
import sys
input = sys.stdin.readline

vowels = list('aeiou')
consonants = list('bcdfghjklmnpqrstvwxyz')

L, C = map(int, input().rstrip().split())
characters = list(input().split())
cases = combinations(characters, L)
answer = []

for case in cases:
    cnt = 0

    for vowel in vowels:
        if vowel in case:
            cnt += 1

    if cnt < 1:
        continue

    elif cnt > L - 2:
        continue

    else:
        sort_case = sorted(case)
        answer.append(''.join(sort_case))

answer.sort()
for ans in answer:
    print(ans)