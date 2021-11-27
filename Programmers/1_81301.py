#!/user/bin/env python3
# -*- coding: utf8 -*-

# 숫자 문자열과 영단어
# https://programmers.co.kr/learn/courses/30/lessons/81301 

def solution(s):
    if s.isdigit():
        return int(s)

    num = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    answer = s
    for n in num:
        answer = answer.replace(n, num[n])
    
    return int(answer)
    

if __name__ == "__main__":
    s = "one4seveneight"
    print(str(solution(s)))
    s = "23four5six7"
    print(str(solution(s)))
    s = "2three45sixseven"
    print(str(solution(s)))
    s = "123"
    print(str(solution(s)))
    