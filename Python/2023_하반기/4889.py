i = 1
while True:
    test = list(input())
    if test[0] == '-':
        break
    stack = list()
    result = 0
    cnt =0 
    for j in range(len(test)):
        if not stack and test[j] == '}': #비어있는데 닫는게 오면
            cnt += 1 #바꿔야 하니까 갯수 더하고
            stack.append('{') #바꿔서 넣는다
        elif stack and test[j] == '}': #닫는게 오는데 비어있지 않으니
            stack.pop() #뽑아주고
        else:
            stack.append(test[j]) #나머지 경우는 넣어준다.
    if stack == 1: #만약 스택에 한개 있으면 무조건 계산 불가라서
        cnt += 1 #이걸 추가하고
    else:
        if len(stack)% 2 == 1: #길이가 2이상이면 절반만 바꾸면 되니까, 근데 홀수
            cnt += len(stack)//2 + 1 
        else: 
            cnt += len(stack)//2 #짝수면 절반만 나누면 됨
    print(str(i) + '. ' + str(cnt)) #결과 값 출력
    i+=1