# 불량 사용자
# https://programmers.co.kr/learn/courses/30/lessons/64064
from itertools import permutations
import re


def check_user(permu, pattern):
    for idx, pt in enumerate(pattern):
        p = re.compile(pt)
        if not p.match(permu[idx]) or len(permu[idx]) != len(pt):
            return False
    return True


def solution(user_id, banned_id):
    ban_pattern = [id.replace('*', '.') for id in banned_id]
    answer = []

    permu = permutations(user_id, len(banned_id))
    
    for p in permu:
        if check_user(p, ban_pattern):
            p = set(p)
            if p not in answer:
                answer.append(p)
    
    return len(answer)


if __name__ == "__main__":
    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["fr*d*", "abc1**"]
    print(solution(user_id, banned_id))
    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["*rodo", "*rodo", "******"]
    print(solution(user_id, banned_id))
    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["fr*d*", "*rodo", "******", "******"]
    print(solution(user_id, banned_id))