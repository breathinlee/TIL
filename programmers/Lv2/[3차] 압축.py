dictionary = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G',
              'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
              'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def solution(msg):
    answer = []
    idx = 0

    while idx < len(msg):
        tmp = msg[idx]

        for k in range(idx + 1, len(msg)):
            tmp += msg[k]
            if tmp not in dictionary:
                break

        if len(tmp) == 1 or tmp in dictionary:
            answer.append(dictionary.index(tmp))
            idx += len(tmp)

        else:
            answer.append(dictionary.index(tmp[:-1]))
            dictionary.append(tmp)
            idx += len(tmp[:-1])

    return answer