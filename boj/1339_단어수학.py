import sys
input = sys.stdin.readline

N = int(input())
answer = 0
alphabet_dict = dict()
for alpha in list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    alphabet_dict[alpha] = 0

for _ in range(N):
    word = input().rstrip()
    for idx in range(len(word)):
        num = 10 ** (len(word) - idx - 1)
        alphabet_dict[word[idx]] += num

sorted_alphabet = sorted(alphabet_dict.items(), key=lambda x: -x[1])
for k in range(26):
    answer += sorted_alphabet[k][1] * (9-k)

print(answer)

# defaultdict 사용하면 알파벳딕셔너리 만들 필요 x