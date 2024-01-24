n = int(input())

cnt = 0
for i in range(n):
    word = list(input())
    stack = []
    for letter in word:
        if stack and stack[-1] == letter:
            stack.pop()
        else:
            stack.append(letter)
    if not stack:
        cnt += 1
print(cnt)   

    