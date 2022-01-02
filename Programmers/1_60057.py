# 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    if len(s) == 1:
        return 1
    
    answer = 1000
    result = ""

    for i in range(1, len(s)//2 + 1):
        pattern = s[:i]
        cnt = 1
        for j in range(i, len(s), i):
            if s[j:i+j] == pattern:
                cnt += 1
            else:
                if cnt == 1:
                    result += pattern
                else:
                    result += f'{cnt}{pattern}'
                    cnt = 1
                pattern = s[j:j+i]
    
        if cnt == 1:
            result += pattern
        else:
            result += f'{cnt}{pattern}'
        
        answer = min(answer, len(result))
        result = ""
        
    return answer


if __name__ == "__main__":
    s = "aabbaccc"
    print(solution(s))
    s = "ababcdcdababcdcd"
    print(solution(s))
    s = "abcabcdede"
    print(solution(s))
    s = "abcabcabcabcdededededede"
    print(solution(s))
    s = "xababcdcdababcdcd"
    print(solution(s))

