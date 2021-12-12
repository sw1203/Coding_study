import math
# 소수찾기
# https://programmers.co.kr/learn/courses/30/lessons/42839

def solution(numbers):
    visit = [0] * len(numbers)
    prime_list = set()

    def make_nums(num=""):
        if num and isprime(int(num)):
            prime_list.add(int(num))
        
        if len(num) == len(numbers):
            return
        
        for idx, _ in enumerate(numbers):
            if visit[idx] == 1:
                continue
            visit[idx] = 1
            make_nums(num+numbers[idx])
            visit[idx] = 0
    
    def isprime(num):
        if num < 2:
            return
        elif num == 2:
            return 2
        else:
            for i in range(2, int(math.sqrt(num)+1)):
                if num % i == 0:
                    return

        return num

    make_nums()

    return len(prime_list)


if __name__ == "__main__":
    print(solution("17"))
    print(solution("011"))
