def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for c in range(len(completion)):
        if participant[c] != completion[c]:
            return participant[c]
    
    return participant[-1]