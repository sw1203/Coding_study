# 베스트앨범
# https://programmers.co.kr/learn/courses/30/lessons/42579

from collections import defaultdict
import heapq

def solution(genres, plays):
    answer = []
    genres_idx = defaultdict(list)
    sum_play = defaultdict(int)

    for idx, genre in enumerate(genres):
        genres_idx[genre].append((idx, plays[idx]))
        sum_play[genre] += plays[idx]
    
    paly_rank = sorted(sum_play.items(), key=lambda x:-x[1])

    for rank in paly_rank:
        genre = rank[0]
        many_play = heapq.nlargest(2, genres_idx[genre], key=lambda x:(x[1], -x[0]))
        answer += [play[0] for play in many_play]
    
    return answer


if __name__ == "__main__":
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    print(solution(genres, plays))