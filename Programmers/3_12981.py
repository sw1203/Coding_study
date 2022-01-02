# 영어 끝말잇기
# https://programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    check = set()

    for idx, word in enumerate(words):
        firstchar = word[0]
        if idx == 0:
            check.add(word)
            lastchar = word[-1]
            continue

        if (word in check) or (firstchar != lastchar):
            return [idx % n + 1, idx // n + 1]
        check.add(word)
        lastchar = word[-1]

    return [0, 0]


if __name__ == "__main__":
    n = 3
    words = [
        "tank", "kick", "know", "wheel", "land",
        "dream", "mother", "robot", "tank"
    ]
    print(solution(n, words))
    n = 5
    words = [
        "hello", "observe", "effect", "take", "either",
        "recognize", "encourage", "ensure", "establish",
        "hang", "gather", "refer", "reference", "estimate", "executive"
    ]
    print(solution(n, words))
    n = 2
    words = [
        "hello", "one", "even", "never", "now", "world", "draw"
    ]
    print(solution(n, words))