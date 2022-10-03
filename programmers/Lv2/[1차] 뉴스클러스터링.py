def solution(str1, str2):
    answer = 1
    c_str1 = []
    c_str2 = []
    
    for k in range(len(str1)-1):
        a, b = str1[k], str1[k+1]
        if a.isalpha() and b.isalpha():
            c_str1.append(a.lower()+b.lower())
    
    for k in range(len(str2)-1):
        a, b = str2[k], str2[k+1]
        if a.isalpha() and b.isalpha():
            c_str2.append(a.lower()+b.lower())
    
    union = c_str1[:]
    copy_union = c_str1[:]
    intersection = []
    
    if len(c_str1) == 0 and len(c_str2) == 0:
        answer *= 65536
    else:
        for s in c_str2:
            if s not in copy_union:
                union.append(s)
            else:
                copy_union.remove(s)
                
        for s in c_str2:
            if s in c_str1:
                c_str1.remove(s)
                intersection.append(s)
            
        answer = int(len(intersection) / len(union) * 65536) 
        
    return answer