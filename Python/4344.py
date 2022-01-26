#bronze1

N=int(input())
for i in range(N):
    grade=list(map(int,input().split()))#리스트 형태로 받기 위한 작업
    
    avg=sum(grade[1:])/grade[0]#앞에 입력 받은 것으로 평균을 2번째부터 계산해 첫번째것으로 나눈뒤에

    cnt=0
    for j in grade[1:]:
        if j>avg:#평균보다 클 때
            cnt+=1#숫자를 더해주고
    rate=cnt/grade[0]*100#원래 인원수만큼 나눠주낟.
    print(f'{rate:.3f}%')#소수점 셋째짜리까지 공개해야 하므로 float형태가 필요. 출력위해 f'{}을 해주고 그 안에 rate:는 그냥 출력 .3f는 셋째까지 출력
