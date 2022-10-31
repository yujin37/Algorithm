def solution(a, b, n):
    answer = 0
    while n>=a:
        cola=n//a #몫구하기
        n%=a #나머지는 바로 반영하면 되므로 계산해주고
        n+=cola*b #n에 몫*대응되는 콜라수를 계산해서 올려주고
        answer+=cola*b #6번 라인에 대한 값을 최종 출력이므로 이 변수에도 추가
    return answer
