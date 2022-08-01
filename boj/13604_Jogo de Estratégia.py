import sys
input = sys.stdin.readline

J, R = map(int, input().split())
points = list(map(int, input().split()))

player_total = [0] * (J+1)

for k in range(J):
    player = 0
    for s in range(R):
        player += points[J*s + k]

    player_total[k+1] = player

winner = -1
result = 0

for i in range(J, -1, -1):
    if result < player_total[i]:
        result = player_total[i]
        winner = i

print(winner)