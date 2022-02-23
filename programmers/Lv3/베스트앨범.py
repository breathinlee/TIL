def solution(genres, plays):
    answer = []
    genre_plays = {}
    genre_total = {}
    
    for g in range(len(genres)):
        if genres[g] in genre_plays.keys():
            genre_plays[genres[g]].append((g, plays[g]))
            genre_total[genres[g]] += plays[g]
        else:
            genre_plays[genres[g]] = [(g, plays[g])]
            genre_total[genres[g]] = plays[g]
    
    sorted_genre_total = sorted(genre_total.items(), key = lambda x: x[1], reverse=True)
    
    for key in sorted_genre_total:
        best_song = genre_plays[key[0]]
        
        best_song = sorted(best_song, key = lambda x: x[1], reverse=True)
        
        if len(best_song) == 1:
            answer.append(best_song[0][0])
        else:
            for v in range(2):  
                answer.append(best_song[v][0])

    return answer