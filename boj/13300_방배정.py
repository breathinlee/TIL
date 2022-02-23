# 같은 성별끼리(0: 여/ 1: 남) + 같은 학년끼리(1~6학년)
# 최소한의 방의 수 출력

N, K = map(int, input().split())  # N: 학생 수 / K: 한 방 최대 인원 수
students = []
for _ in range(N):
    S, Y = map(int, input().split())
    students.append((S, Y))
girls_grade_cnt = [0] * 7
boys_grade_cnt = [0] * 7
for student in students:
    if student[0] == 0:
        for i in range(1, 7):
            if student[1] == i:
                girls_grade_cnt[i] += 1
    elif student[0] == 1:
        for i in range(1, 7):
            if student[1] == i:
                boys_grade_cnt[i] += 1
ans = 0
for i in range(1, 7):
    if boys_grade_cnt[i] == 0:
        continue
    elif boys_grade_cnt[i] <= K:
        ans += 1
    else:
        if boys_grade_cnt[i] % K:
            ans += (boys_grade_cnt[i] // K) + 1
        else:
            ans += (boys_grade_cnt[i] // K)
for i in range(1, 7):
    if girls_grade_cnt[i] == 0:
        continue
    elif girls_grade_cnt[i] <= K:
        ans += 1
    else:
        if girls_grade_cnt[i] % K:
            ans += (girls_grade_cnt[i] // K) + 1
        else:
            ans += (girls_grade_cnt[i] // K)
print(ans)