import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    line = list(input().strip())
    check = list()
    result = True
    for ps in line:
        if ps == '(':
            check.append('(')
        elif ps == ')':
            if len(check) > 0 and check[-1] == '(':
                check.pop()
            else:
                check.append(')')
    if len(check) == 0:
        print('YES')
    else:
        print('NO')
