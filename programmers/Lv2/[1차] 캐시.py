# LRU(Least Recently Used) 알고리즘

def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.remove(city)
            
        else:
            if len(cache) == cacheSize:
                cache.pop(0)
            answer += 5
        cache.append(city)
            
    return answer