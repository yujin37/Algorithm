#브론즈2, 재귀의 귀재, 재귀 복습차원
global cnt_recursive #함수에서도 사용하기 위해 글로벌 변수 지정
def recursion(answer, l, r):
    global cnt_recursive
    cnt_recursive +=1 #호출해 진입하면 갯수 세주기
    if(l>=r): #조건문은 문제에서 주어졌으므로 복사
        return 1
    elif(answer[l] != answer[r]):
        return 0
    else:
        return recursion(answer, l+1, r-1)
def isPalindrom(answer):
    return recursion(answer,0,len(answer)-1)

n=int(input())
for i in range(n):
    cnt_recursive=0 #이 변수만 글로벌 변수로 매번 초기화
    answer=input() #문자열 입력
    pall=isPalindrom(answer) #리턴 값을 담아줌.
    print(pall, cnt_recursive) #결과 출력
