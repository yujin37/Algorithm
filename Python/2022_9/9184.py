#실버2, 신나는 함수 실행, 동적프로그래밍 연습
def w(a,b,c):
    if a<=0 or b<=0 or c<=0: #이건 기존 예시 동일
        return 1
    elif a>20 or b>20 or c>20: #기존 예시 동일
        return w(20,20,20)
    if total[a][b][c]:
        return total[a][b][c] #일단 빠르게 하기 위해 배열에 속하는 것이 있으면 바로 리턴해주고
    if a<b and b<c:
        total[a][b][c]=w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c) #이건 배열에 return 대신 넣어주고
    else:
        total[a][b][c]=w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1) #이것 역시 배열에 return 대신 넣어준다.
    return total[a][b][c] #위 세개의 경우에 리턴이 없기 때문에 이를 해결하기 위한 리턴을 만들어준다.
total=[[[0]*21 for _ in range(21) ] for _ in range(21)] #이건 최대 20^3개의 배열을 만들기 위한 작업이다.
while True: 
    a,b,c=map(int,input().split()) 
    if a==-1 and b==-1 and c==-1: #이건 탈출조건
        break
    print('w(%d, %d, %d)= %d' %(a,b,c, w(a,b,c))) #호출을 통해 결과값 호출
