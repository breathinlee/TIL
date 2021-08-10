# 백준 11650번 좌표 정렬하기
"""
2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
"""

n = int(input())
x, y = list(map(int, input(). split()))

for i in range(1, n+1):
    print(i)
    # if x_list[i-1] < x_list[i]:
    #     print(x_list[i-1], y_list[i-1])
    # elif x_list[i-1] == x_list[i]:
    #     if y_list[i-1] < y_list[i]:
    #         print(x_list[i-1], y_list[i-1])
    #     else:
    #         print(x_list[i], y_list[i])
    # else:
    #     print(x_list[i], y_list[i])