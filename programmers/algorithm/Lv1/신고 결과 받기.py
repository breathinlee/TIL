def solution(id_list, report, k):
    answer = [0] * len(id_list)
    result = {}
    who_report = {id: [] for id in id_list}
    be_reported = []
    
    report = set(report)
    for r in report:
        reporting, reported = r.split(' ')
        
        who_report[reporting].append(reported)
        
        if reported not in result:
            result[reported] = 1
        else:
            result[reported] += 1
            
    for key, value in result.items():
        if value >= k:
            be_reported.append(key)
            
    for k, v in who_report.items():
        for b in be_reported:
            if b in v:
                answer[id_list.index(k)] += 1
    
    return answer