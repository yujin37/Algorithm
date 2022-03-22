#bronze3/ 이 문제는 10952문제와 달리 오류 발생 시 break를 거는 형태
while True:
    try:#이를 위해 try except를 이용한다. 오류가 없다면 입력을 받아 출력
        A,B=map(int, input().split())
        print(A+B)
    except:#그렇지 않다면 오류
        break
