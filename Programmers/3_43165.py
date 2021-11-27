# 타겟넘버
# https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    answer = 0
    def dfs(idx, total):
        if idx == len(numbers):
            if total == target:
                # nonlocal 이 사용된 함수 바로 한단계 바깥쪽에 위치한 변수와 바인딩을 할 수 있다. 전역변수는 제외
                nonlocal answer
                answer += 1
            return 
            
        dfs(idx+1, total+numbers[idx])
        dfs(idx+1, total-numbers[idx])

    dfs(0,0)
    return answer


if __name__ == "__main__":
    numbers = [1, 1, 1, 1, 1]
    target = 3
    print(solution(numbers, target))
    