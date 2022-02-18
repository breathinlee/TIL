def solution(s):
    answer = False
    if len(s) == 4 or len(s) == 6:
        for st in s:
            if not st.isdigit():
                break
        else:
            answer = True
    return answer