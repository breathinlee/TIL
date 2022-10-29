def calculateTime(time):
    return int(time[:2])*60+int(time[3:])


def solution(n, t, m, timetable):
    answer = ''
    crewTime = sorted([calculateTime(time) for time in timetable])
    busTime = 540
    
    idx = 0
    cr = 0
    while idx < n:
        passenger = 0
        
        while (cr < len(crewTime) and passenger < m and crewTime[cr] <= busTime):
            cr += 1
            passenger += 1
            
        if passenger < m:  # 버스에 자리 남은경우
            answer = busTime
        
        else: # 버스에 자리가 없으면 이전에 탄 크루보다 1분 먼저
            answer = crewTime[cr-1]-1
            
        idx += 1
        busTime += t
    
    return '%02d:%02d'%(answer//60, answer%60)