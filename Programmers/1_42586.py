# 기능개발
# https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []
    stack = []
    
    for p, s in zip(progresses, speeds):
        todo = 100 - p 
        if todo % s != 0:
            worktimes = todo//s + 1
        else:
            worktimes = todo//s
        
        if not stack:
            stack.append(worktimes)
        elif worktimes > stack[0]:
                answer.append(len(stack))
                stack.clear()
                stack.append(worktimes)
        else:
            stack.append(worktimes)

    if stack:
        answer.append(len(stack))
        
    return answer
      

if __name__ == "__main__":
    progresses = [93, 30, 55]
    speeds = [1, 30, 5]
    print(solution(progresses, speeds))

    progresses = [95, 90, 99, 99, 80, 99]
    speeds = [1, 1, 1, 1, 1, 1]
    print(solution(progresses, speeds))
