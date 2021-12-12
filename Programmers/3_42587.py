from collections import deque
# 프린터
# https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    jobs = deque()
    stack = []

    for idx, priority in enumerate(priorities):
        jobs.append([priority, idx])
    
    while jobs:
        prior = jobs.popleft()
        
        if not jobs:
            stack.append(prior[1])
            break

        if prior[0] < max(jobs)[0]:
            jobs.append(prior)
        else:
            stack.append(prior[1])
    
    return stack.index(location) + 1


if __name__ == "__main__":
    priorities = [2, 1, 3, 2]
    location = 2
    print(solution(priorities, location))
    priorities = [1, 1, 9, 1, 1, 1]
    location = 0
    print(solution(priorities, location))