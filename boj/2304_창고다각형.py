N = int(input())
column_data = [tuple(map(int, input().split())) for _ in range(N)]
column_data.sort(key=lambda x: x[1])

max_idx, max_height = column_data.pop()
left_idx = max_idx
right_idx = max_idx
area = max_height

while column_data:
    idx, h = column_data.pop()

    if idx < left_idx:
        area += (left_idx - idx) * h
        left_idx = idx
    elif idx > right_idx:
        area += (idx - right_idx) * h
        right_idx = idx

print(area)



# 틀린 풀이 (반례 ㅇ)
"""
# 전체에서 빼지말고 넓이 구해서 더하는 식으로 해야 한다.

N = int(input())
column = []
my_height = []
for _ in range(N):
    L, H = map(int, input().split())   # L : 각 기둥의 왼쪽 면의 위치 H: 높이
    column.append((L, H))
    my_height.append(H)
column.sort(key=lambda x: x[0])
base = column[-1][0] - column[0][0] + 1    # 밑변의 길이
max_height = 0                             # 가장 긴 높이
max_height_idx = 0
for case in column:
    if case[1] > max_height:
        max_height = case[1]
        max_height_idx = column.index(case)
max_area = base * max_height
# print(max_height_idx)
height = column[0][1]
length = []
tmp = []
start = 0
idx = 1
while idx < max_height_idx+1:
    if column[start][1] < column[idx][1]:
        length.append(column[idx][0] - column[start][0])
        tmp.append(max_height - column[start][1])
        start = idx
    idx += 1

for i in range(len(length)):
    max_area -= (length[i] * tmp[i])

if max_height_idx != N-1:
    if my_height.count(max_height) > 1:
        for k in range(max_height_idx+1, N):
            if max_height == column[k][1]:
                last_length = column[-1][0] - column[k][0]
                last_height = 0
                for j in range(k + 1, N):
                    if last_height < column[j][1]:
                        last_height = column[j][1]
    else:
        last_length = column[-1][0] - column[max_height_idx][0]
        last_height = 0
        for j in range(max_height_idx+1, N):
            if last_height < column[j][1]:
                last_height = column[j][1]

    max_area -= (max_height - last_height)*last_length

print(max_area)


반례

5
1 4
2 5
3 6
4 5
5 4

답: 24
"""