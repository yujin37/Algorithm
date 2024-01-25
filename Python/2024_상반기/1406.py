import sys
input = sys.stdin.readline

editor = list(input().strip()) #초기에 편집기에 입력되어있는 문자열
stack = list()


m = int(input()) #입력할 명령어의 개수를 나타냄s
for i in range(m):
    message = list(input().split())
    
    if message[0] == "L": #커서를 왼쪽으로 한 칸 옮김
        if editor:
            stack.append(editor.pop())
    elif message[0] == "D": #커서를 오른쪽으로 한 칸 옮김
        if stack:
            editor.append(stack.pop())

    elif message[0] == "B": #커서 왼쪽에 있는 문자를 삭제함 
        if editor:
            editor.pop()
    elif message[0] == "P":
        editor.append(message[1])

editor.extend(reversed(stack))
print("".join(editor))