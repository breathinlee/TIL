import sys
input = sys.stdin.readline

N = int(input())
switches = list(map(int, input().strip().split()))
student_cnt = int(input())
change_case = [list(map(int, input().strip().split())) for _ in range(student_cnt)]

for k in range(student_cnt):
    if change_case[k][0] == 1:
        tmp = change_case[k][1]
        cnt = 1
        while tmp * cnt <= len(switches):
            if switches[tmp*cnt - 1]:
                switches[tmp * cnt - 1] = 0
            else:
                switches[tmp * cnt - 1] = 1

            cnt += 1

    else:
        tmp = change_case[k][1]
        cnt = 1
        while tmp - cnt >= 1 and tmp + cnt <= len(switches):
            if switches[tmp - cnt - 1] == switches[tmp + cnt - 1]:
                cnt += 1
            else:
                break

        for k in range(cnt):
            if switches[tmp - k - 1]:
                switches[tmp - k - 1] = switches[tmp + k - 1] = 0
            else:
                switches[tmp - k - 1] = switches[tmp + k - 1] = 1

for i in range(1, N+1):
    print(switches[i-1], end=' ')
    if i % 20 == 0:
        print()