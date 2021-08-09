# swea 1206. view
"""
강변에 빌딩들이 옆으로 빽빽하게 밀집한 지역이 있다.
이곳에서는 빌딩들이 너무 좌우로 밀집하여, 강에 대한 조망은 모든 세대에서 좋지만 왼쪽 또는 오른쪽 창문을 열었을 때 바로 앞에 옆 건물이 보이는 경우가 허다하였다.
그래서 이 지역에서는 왼쪽과 오른쪽으로 창문을 열었을 때, 양쪽 모두 거리 2 이상의 공간이 확보될 때 조망권이 확보된다고 말한다.
빌딩들에 대한 정보가 주어질 때, 조망권이 확보된 세대의 수를 반환하는 프로그램을 작성하시오.
아래와 같이 강변에 8채의 빌딩이 있을 때, 연두색으로 색칠된 여섯 세대에서는 좌우로 2칸 이상의 공백이 존재하므로 조망권이 확보된다. 따라서 답은 6이 된다.
"""

for k in range(1, 11):   # 총 10개의 tc
    N = int(input())
    numbers = list(map(int, input(). split()))
    cnt = 0  # 조망권이 확보되는 세대의 수를 0으로 초기화
    for i in range(2, N - 2):   # i번째 빌딩에 대하여 양쪽 모두 거리가 2 이상의 공간이 확보될 떄, 조망권이 확보되므로 i-2, i-1, i+1, i+2 이렇게 4개와 비교해야 함.
        if numbers[i] > numbers[i - 2] and numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1] and numbers[i] > numbers[i + 2]:
            # 주변 네개의 빌딩과 비교했을 때, 모두 i 번째가 더 클 경우에만 조망권이 확보되는 세대 수가 생길 수 있음
            data = [numbers[i - 2], numbers[i - 1], numbers[i + 1], numbers[i + 2]]
            max_data = data[0]
            for j in range(4):   # 주변 i-2, i-1, i+1, i+2 번째 빌딩의 높이 중 가장 높은 것을 고르기 위함
                if data[j] > max_data:
                    max_data = data[j]
                    j += 1
            # max_data = max(numbers[i-2], numbers[i-1], numbers[i+1], numbers[i+2])
            cnt += numbers[i] - max_data   # 조망권이 확보되는 세대의 수는 i번째 빌딩에서 i-2, i-1, i+1, i+2 번째 빌딩 중 가장 높은 것과의 차이이므로 cnt에 더함
            i += 1
        else:
            continue
    print("#{} {}".format(k, cnt))