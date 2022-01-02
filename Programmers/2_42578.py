# 위장
# https://programmers.co.kr/learn/courses/30/lessons/42578

from collections import defaultdict

def solution(clothes):
    answer = 1
    closet = defaultdict(int)
    
    for _, category in clothes:
        closet[category] += 1
    
    for category in closet:
        answer *= closet[category] + 1
    
    return answer - 1
    

if __name__ == "__main__":
    clothes = [
        ["yellowhat", "headgear"],
        ["bluesunglasses", "eyewear"],
        ["green_turban", "headgear"]
    ]
    print(solution(clothes))
    clothes = [
        ["crowmask", "face"],
        ["bluesunglasses", "face"],
        ["smoky_makeup", "face"]
    ]
    print(solution(clothes))
