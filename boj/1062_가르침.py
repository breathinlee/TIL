from itertools import combinations
import sys

input = sys.stdin.readline

def count_words(words, learning):
    cnt = 0
    for word in words:
        for w in word:
            if w not in learning:
                break
        else:
            cnt += 1

    return cnt


N, K = map(int, input().split())
words = [set(input()[4:-4]) for _ in range(N)]
answer = 0

if K < 5 or K == 26:
    print(N) if K == 26 else print(0)
else:
    for word in words:
        for w in ('a', 'n', 't', 'i', 'c'):
            if w in word:
                word.remove(w)

    union_words = set()
    for word in words:
        union_words = union_words | word

    if len(union_words) <= K-5:
        print(N)
    else:
        cases = list(combinations(union_words, K-5))
        for case in cases:
            cnt = count_words(words, set(case))

            if cnt > answer:
                answer = cnt

        print(answer)
