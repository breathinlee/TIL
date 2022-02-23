N, M = map(int, input().split())   # N : 가로 M : 세로 (최대 100)
cutting = int(input())
how_to_cut = [list(map(int, input().split())) for _ in range(cutting)]
how_to_cut.sort(key=lambda x: (x[0], x[1]))

sero = []
garo = []
for way in how_to_cut:
    if way[0] == 0:
        sero.append(way[1])
    else:
        garo.append(way[1])

sero = [0] + sero + [M]
garo = [0] + garo + [N]

max_sero = 0
for i in range(len(sero) - 1):
    sero_length = sero[i+1] - sero[i]
    if max_sero < sero_length:
        max_sero = sero_length

max_garo = 0
for i in range(len(garo) - 1):
    garo_length = garo[i+1] - garo[i]
    if max_garo < garo_length:
        max_garo = garo_length

print(max_garo*max_sero)