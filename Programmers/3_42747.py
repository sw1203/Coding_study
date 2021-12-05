# H-Index
# https://programmers.co.kr/learn/courses/30/lessons/42747


def solution(citations):
    citations.sort(reverse=True)
    for idx, citation in enumerate(citations):
        if idx >= citation:
            return idx

    return len(citations)


if __name__ == "__main__":
    citations = [3, 0, 6, 1, 5]
    print(solution(citations))
        