import sys
input = sys.stdin.readline

n = int(input())
stack = list()
now = 1
result = []
for i in range(n):
    num = int(input())
    while now <= num:
        stack.append(now)
        result.append('+')
        now += 1
    if stack[-1] == num:
        stack.pop()
        result.append('-')
if stack:
    print('NO')
else:
    for val in result:
        print(val)