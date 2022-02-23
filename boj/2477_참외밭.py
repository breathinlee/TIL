K = int(input())    # 참외의 개수
arr = [list(map(int, input().split())) for _ in range(6)]
cnt = [0] * 5
for direction, length in arr:
    cnt[direction] += 1

for i in range(6):
    if cnt[arr[i][0]] == 1 and cnt[arr[(i+1)%6][0]] == 1:
        ab = arr[i][1] * arr[(i+1)%6][1]
        cd = arr[(i+3)%6][1] * arr[(i+4)%6][1]
        break

print((ab-cd)*K)