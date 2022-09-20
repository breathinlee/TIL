def solution(s):
    stack = []
    
    for k in s:
        if k == '(':
            stack.append(k)
        elif stack and k == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(k)
        else:
            return False
    
    if stack:
        return False
    
    return True