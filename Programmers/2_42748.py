#!/user/bin/env python3
# -*- coding: utf8 -*-

# K번째 수
# https://programmers.co.kr/learn/courses/30/lessons/42748 

def solution(array, commands):
    return [sorted(array[c[0]-1:c[1]])[c[2]-1] for c in commands]


if __name__ == "__main__":
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [
        [2, 5, 3],
        [4, 4, 1],
        [1, 7, 3]
    ]
    print(solution(array, commands))
