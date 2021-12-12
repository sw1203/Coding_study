from itertools import permutations
import math
# 소수찾기
# https://programmers.co.kr/learn/courses/30/lessons/42839

def solution(numbers):
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
    
    num_list = set()
    
    for idx, _ in enumerate(numbers):
        num_list |= set(map(int, map("".join, permutations(list(numbers), idx + 1))))
    num_list -= set(range(0, 1))
    
    prime = [] 
    for n in num_list:
        if isprime(n):
            prime.append(n)
    
    return len(prime)
    

if __name__ == "__main__":
    print(solution("17"))
    print(solution("011"))
