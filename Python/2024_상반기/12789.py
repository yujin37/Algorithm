n = int(input())
line = list(map(int,input().split()))
stack = []
result = []
now = 1
i = 0
while now <= n:
    if i < len(line) and now == line[i]: #위치에 있는 숫자가 있으면
        result.append(now) #결과에 추가해주고 
        i += 1 #한 칸 이동
        now += 1 #숫자도 증가시킨다. 
    elif stack and now == stack[-1]: #스택에 있으면 넣어주고
        stack.pop()#있는 숫자를 제거한다.
        result.append(now)
        now += 1 #숫자 증가시키기
    else: #두군데 다 없으면 
        if i < len(line): #만약 범위 안에 인덱스가 돌고 있으면
            stack.append(line[i]) #스택에 추가시키고
            i += 1 #인덱스 한칸 이동
        else: #초과하면 바로 탈출
            break

if stack: #끝났는데도 스택이 남아있으면
    print("Sad")
else:
    print("Nice")
    