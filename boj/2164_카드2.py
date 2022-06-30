from collections import deque
import sys

N = int(input())
cards = deque([n for n in range(1, N+1)])

while len(cards) > 1:
    cards.popleft()
    tmp = cards.popleft()
    cards.append(tmp)

print(cards[0])