def solution(files):
    answer = []
    for idx, file in enumerate(files):
        head = ''
        number = ''
        flag = False
        for f in file:
            if f.isdigit():
                flag = True
                number += f
            elif flag and not f.isdigit():
                break
            else:
                head += f

        answer.append([head.lower(), int(number), idx, file])

    answer.sort()

    return [a[3] for a in answer]