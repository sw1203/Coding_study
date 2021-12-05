# 거리두기 확인하기
# https://programmers.co.kr/learn/courses/30/lessons/81302

def solution(places):
    answer = []
    size = 5
    
    def valid(r, c):
        return -1<r<size and -1<c<size
    
    def check(x, y, place):
        # 상하좌우
        dist = [(1,0),(0,1),(-1,0),(0,-1)]
        for dx, dy in dist:
            nx, ny = x+dx, y+dy
            if valid(nx, ny) and place[nx][ny]=='P':
                return False
        
        # 대각선
        dist = [(-1,-1),(-1,1),(1,-1),(1,1)]
        for dx, dy in dist:
            nx, ny = x+dx, y+dy
            if valid(nx, ny) and place[nx][ny]=='P' and (place[x][ny]!='X' or place[nx][y]!='X'):
                return False
        
        # 거리가 2인 상하좌우
        dist = [(2,0), (0,2), (-2,0), (0,-2)]
        for dx, dy in dist:
            nx, ny = x+dx, y+dy
            if valid(nx, ny) and place[nx][ny] =='P' and place[x+dx//2][y+dy//2] !='X':
                return False
        return True
    
    for place in places:
        flag = True
        for r, c in [(i, j) for i in range(5) for j in range(5)]:
            if place[r][c] == 'P':
                result = check(r,c, place)
                if not result:
                    answer.append(0)
                    flag = False
                    break
        if flag:
            answer.append(1)
        
    return answer


if __name__ == "__main__":
    places = [
        ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
        ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
        ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
        ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
        ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
    ]
    print(solution(places))