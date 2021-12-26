# 로또의 최고 순위와 최저 순위
# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    rank = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
    }
    zeros = lottos.count(0)
    count = 0

    for num in lottos:
        if num in win_nums:
            count += 1
    
    return [rank.get(count+zeros, 6), rank.get(count, 6)]


if __name__ == "__main__":
    lottos = [44, 1, 0, 0, 31, 25]
    win_nums = [31, 10, 45, 1, 6, 19]
    print(solution(lottos, win_nums))
    lottos = [0, 0, 0, 0, 0, 0]
    win_nums = [38, 19, 20, 40, 15, 25]
    print(solution(lottos, win_nums))
    lottos = [45, 4, 35, 20, 3, 9]
    win_nums = [20, 9, 3, 45, 4, 35]
    print(solution(lottos, win_nums))
    