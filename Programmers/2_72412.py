import copy
from collections import defaultdict
from itertools import combinations
# 순위 검색
# https://programmers.co.kr/learn/courses/30/lessons/72412

def solution(information:list, query:list) -> list:
    applicant = defaultdict(list)
    answer = []
    make_applicant_dict(information, applicant)
    sortscore(applicant)
    for q in query:
        split_query = [word for word in q.split() if word != "and"]
        answer.append(count_people(split_query, applicant))
    return answer

def make_applicant_dict(information:list, applicant:defaultdict):
    for info in information:
        i = [word for word in info.split() if word != "and"]
        conditions = i[:-1]
        score = int(i[-1])
        for r in range(5):
            combis = list(combinations(range(4), r))
            for c in combis:
                case = copy.deepcopy(conditions)
                for v in c:
                    case[v] = "-"
                applicant["/".join(case)].append(score)
    
def sortscore(applicant:defaultdict):
    for key in applicant:
        applicant[key].sort()

def count_people(split_query:list, applicant:defaultdict):
    conditions = "/".join(split_query[:-1])
    score = int(split_query[-1])
    
    # query에 일치하는 것이 information에 없을 수도 있다.
    if conditions in applicant:
        data = applicant[conditions]
        start, end = 0, len(data)
        while start != end and start != len(data):
            mid = (start + end) // 2
            if data[mid] >= score:
                end = mid
            else:
                start = mid + 1
        return len(data) - start 

    else:
        return 0


if __name__ == "__main__":
    information = [
        "java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"
    ]
    query = [
        "java and backend and junior and pizza 100",
        "python and frontend and senior and chicken 200",
        "cpp and - and senior and pizza 250",
        "- and backend and senior and - 150",
        "- and - and - and chicken 100",
        "- and - and - and - 150"
    ]
    print(solution(information, query))
    