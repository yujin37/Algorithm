#bronze2
N=int(input())
for i in range(N):
    sum=0
    count=1
    test=list(input())#리스트형태로 받을 수 있도록 한다.
    for j in test:#test안에 있는 각 ox들이 존재할때
        if(j=='O'):#o라면 
            sum+=count#sum에 count해주고
            count+=1#이거는 연속 맞출때 그만큼 각 점수가 증가한다.
        elif(j=='X'):#틀린다면
            count=1#count를 초기화해주어야 하므로 1로 초기화
    print(sum)#각 테스트당 보여주어야 하므로 내부 for문 끝나면 바로바로 출력
