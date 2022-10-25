def replacing(s):
    s=s.replace('C#', 'c')
    s=s.replace('D#', 'd')
    s=s.replace('E#', 'e')
    s=s.replace('F#', 'f')
    s=s.replace('G#', 'g')
    s=s.replace('A#', 'a')
    return s


def calculateTime(str1, str2):
    h1, m1 = map(int, str1.split(':'))
    h2, m2 = map(int, str2.split(':'))
    remain = 0
    
    if m1 <= m2:
        remain += (60*(h2 - h1) + (m2 - m1))
    else:
        h2 -= 1
        m2 += 60
        remain += (60*(h2 - h1) + (m2 - m1))
            
    return remain
        
    
def solution(m, musicinfos):
    answer = ''
    m = replacing(m)
    musicDict = dict()
    
    for idx, infos in enumerate(musicinfos):
        s, e, title, info = infos.split(',')
        info = replacing(info)
        playing = calculateTime(s, e)
        if playing < len(info):
            musicDict[title] = [idx, playing, info[:playing], title]
        elif playing == len(info):
            musicDict[title] = [idx, playing, info, title]
        else:
            tmp = playing // len(info)
            newInfo = info*tmp + info[:playing % len(info)]
            musicDict[title] = [idx, playing, newInfo, title]
    
    musicList = sorted(musicDict.values(), key=lambda x: (-x[1], x[0]))

    for music in musicList:
        if m in music[2]:
            answer = music[3]
            break
    
    else:
        answer = "(None)"
    
    return answer