#!/user/bin/env python3
# -*- coding: utf8 -*-

# 모의고사
# https://programmers.co.kr/learn/courses/30/lessons/42840 

def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    count = [0, 0, 0]

    len_first = len(first)
    len_second = len(second)
    len_third = len(third)

    for idx , answer in enumerate(answers):
        if answer == first[idx % len_first]:
            count[0] += 1
        if answer == second[idx % len_second]:
            count[1] += 1
        if answer == third[idx % len_third]:
            count[2] += 1
    
    max_count = max(count)
    answer = []
    
    for idx, c in enumerate(count):
        if c == max_count:
            answer.append(idx + 1)
    return answer


if __name__ == "__main__":
    answers = [1, 2, 3, 4, 5]
    print(solution(answers))
    
    answers = [1, 3, 2, 4, 2]
    print(solution(answers))
