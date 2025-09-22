def solution(s):
    answer = True
    stack = list()
    for check in s:
        if check == ")" and not stack: #만약 닫는 괄호인데 스택이 비어있으면
            return False #바로 되돌려주고
        if check == ")" and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(check)
    if not stack:
        return True
    return False
s = "(()("
print(solution(s))