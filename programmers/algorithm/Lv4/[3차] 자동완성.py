def compare(a, b):
    result = 0

    for s in range(min(len(a), len(b))):
        if a[s] == b[s]:
            result += 1
        else:
            result += 1
            break
    else:
        if len(a) > len(b):
            result += 1

    return result


def solution(words):
    answer = 0
    sorted_words = sorted(words)
    cnt = [0] * len(words)

    for k in range(len(words)):
        if k == 0:
            cnt[k] = compare(sorted_words[k], sorted_words[k+1])

        elif k == len(words) - 1:
            cnt[k] = compare(sorted_words[k], sorted_words[k-1])

        else:
            ret1 = compare(sorted_words[k], sorted_words[k-1])
            ret2 = compare(sorted_words[k], sorted_words[k+1])

            cnt[k] = max(ret1, ret2)

    answer = sum(cnt)

    return answer