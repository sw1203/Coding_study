# 오픈채팅방
# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record_list):
    user_info = {}

    for record in record_list:
        if record[0] in ["E", "C"]:
            sentence = record.split()
            id = sentence[1]
            name = sentence[2]
            user_info[id] = name

    return make_sentences(record_list, user_info)

def make_sentences(record_list, user_info):
    result = []
    printer = {
        "E": "님이 들어왔습니다.",
        "L": "님이 나갔습니다."
    }
    for record in record_list:
        if record[0] in ["E", "L"] :
            sentence = record.split()
            id = sentence[1]
            result.append(f"{user_info[id] + printer[record[0]]}")
    
    return result


if __name__ == "__main__":
    record_list = [
        "Enter uid1234 Muzi", 
        "Enter uid4567 Prodo",
        "Leave uid1234",
        "Enter uid1234 Prodo",
        "Change uid4567 Ryan"
    ]
    
    print(solution(record_list))
