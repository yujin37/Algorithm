def solution(number, k):
    answer = ''
    stack = []
    length = len(number)-k #최종 스택
    for num in number:
        if not stack: #비어있을 때
            stack.append(num)
            continue
        if k>0: #두번째 부터 시작하게 됨
            while stack[-1] < num: #기존 것이 새로운 숫자보다 작으면
                stack.pop() #기존거 뽑고
                k-=1 #개수 감소, 작은 숫자 제거
                if not stack or k <= 0: #비어있거나 k가 0보다 작아지면
                    break #그만둔다.
        stack.append(num) #그리고 현재 숫자를 등록
    
    for i in range(length): #만약 4321처럼 나오면 그대로 오므로 길이만큼 잘라낸다.
        answer += stack[i]

    return answer
print(solution("4321", 1))