def check(result):  #주변을 체크하는 함수
    for x,y,a in result:
        if a == 0:  #기둥이라면, 불가능 한 경우 제시
            if y!=0 and (x,y-1,0) not in result and \
            (x-1,y,1) not in result and (x,y,1) not in result:
                return True
        else: #보이라면, 불가능 한 경우 제시
            if(x,y-1,0) not in result and (x+1, y-1,0) not in result and \
            not ((x-1,y,1) in result and (x+1, y, 1) in result):
                return True
    return False
        
def solution(n, build_frame):
    result = set()
    for frame in build_frame:
        #print('진행',build_frame[i][3])
        frame_x = frame[0]
        frame_y = frame[1]
        frame_type = frame[2]
        frame_state = frame[3]
        if frame_state == 1: #만약 설치하라고 하면
            result.add((frame_x, frame_y,frame_type)) #일단 추가하고
            if check(result): #설치 가능하지 확인해서 불가능하다고 하면
                result.remove((frame_x, frame_y, frame_type)) #제거
        elif (frame_x,frame_y,frame_type) in result: #만약 삭제하라고 하면
            result.remove((frame_x, frame_y, frame_type)) #일단 제거하고
            if check(result): #체크했는데 불가능하다면
                result.add((frame_x, frame_y,frame_type)) #무시하도록 추가한다.
    answer = map(list, result) #set 형태를 리스트형태로 변환하고
 
    return sorted(answer, key = lambda x: (x[0], x[1], x[2])) #정렬, 오름차순

n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
print(solution(n, build_frame)) #예상 답: [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
print('----------')
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n, build_frame)) #예상 답: [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]