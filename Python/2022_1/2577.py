#bronze2/ 다시 풀기
total=1#곱하기 위해 1로 설정
for i in range(3):#세번 입력 받는 for문
    total*=(int(input()))#입력받아서 total에 바로 곱해주고
result=list(str(total))#이것을 문자화 시켜서 리스트를 result에 넣는다.
for i in range(10):#0부터 9까지 이므로 10개를 해주고
    print(result.count(str(i)))#count(숫자)가 몇개 있는지 세주는 것이 .count의 역할이다. 그리고 바로 출력
