import sys
input = sys.stdin.readline

def grouping(word):
    character = dict()
    character[word[0]] = 1

    idx = 1

    while idx < len(word):
        tmp = word[idx - 1]

        if word[idx] not in character:
            character[word[idx]] = 1

        elif word[idx] in character and tmp == word[idx]:
            character[word[idx]] += 1

        else:
            return False

        idx += 1

    return True


N = int(input())
words = [input().rstrip() for _ in range(N)]

cnt = 0

for word in words:
    if grouping(word):
        cnt += 1

print(cnt)