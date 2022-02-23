def solution(w,h):
    area = w * h
    wh_sum = w + h
    
    while w != h:
        if w > h: 
            w -= h
        else: 
            h -= w

    return area - (wh_sum - w)