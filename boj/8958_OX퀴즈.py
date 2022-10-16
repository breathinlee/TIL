T = int(input())
for _ in range(T):
    quiz = input()
    total = 0
    score = 0
    for k in range(len(quiz)):
        if quiz[k] == 'O':
            score += 1
            total += score
        else:
            score = 0

    print(total)