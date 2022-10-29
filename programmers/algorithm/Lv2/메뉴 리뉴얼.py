from collections import defaultdict
from itertools import combinations

def solution(orders, courses):
    answer = []

    for course in courses:
        c_dict = defaultdict(int)
        for order in orders:
            order = sorted(order)
            cases = list(combinations(order, course))
            for case in cases:
                c_dict[case] += 1

        c_list = sorted(c_dict.items(), key=lambda x: x[1], reverse=True)

        if len(c_list):
            max_num = c_list[0][1]
            if max_num >= 2:
                for key, value in c_dict.items():
                    j_key = ''.join(key)
                    if value == max_num and j_key not in answer:
                        answer.append(''.join(key))

    return sorted(answer)