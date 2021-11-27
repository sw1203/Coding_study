import math
# 나머지가 1이 되는 수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    if (n - 1) % 2 == 0:
        return 2
    
    # n - 1이 소수인지 판별
    for answer in range(2, int(math.sqrt(n - 1)) + 1):
        if (n - 1) % answer == 0:
            return answer
    
    return n - 1


if __name__ == "__main__":
    print(solution(10))
    print(solution(12))
