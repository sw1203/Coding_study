# 다리를 지나는 트럭
# https://programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    q = deque([0] * bridge_length)
    idx = 0
    sum_w = 0
    
    while q:
        if w:=q.popleft():
            sum_w -= w
        time += 1
        if idx < len(truck_weights):
            if sum_w + truck_weights[idx] <= weight:
                sum_w += truck_weights[idx]
                q.append(truck_weights[idx])
                idx += 1
            else:
                q.append(0)
    
    return time


if __name__ == "__main__":
    bridge_length = 2
    weight = 10
    truck_weights = [7,4,5,6]
    print(solution(bridge_length, weight, truck_weights))
    bridge_length = 100
    weight = 100
    truck_weights =	[10]
    print(solution(bridge_length, weight, truck_weights))
    bridge_length = 100
    weight = 100
    truck_weights = [10,10,10,10,10,10,10,10,10,10]
    print(solution(bridge_length, weight, truck_weights))
