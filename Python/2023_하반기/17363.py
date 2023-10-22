n, m = map(int,input().split())
program = list()
for i in range(n):
    tmp = list(input())
    for j in range(m):
        if tmp[j] == '.':
            tmp[j] = '.'
        elif tmp[j] == 'O':
            tmp[j] = 'O'
        elif tmp[j] == '-':
            tmp[j] = '|'
        elif tmp[j] == '|':
            tmp[j] = '-'
        elif tmp[j] == "/":
            tmp[j] =  "\\"
        elif tmp[j] =="\\":
            tmp[j] = "/"
        elif tmp[j] == '^':
            tmp[j] = '<'
        elif tmp[j] == '<':
            tmp[j] = 'v'
        elif tmp[j] == 'v':
            tmp[j] = '>'
        elif tmp[j] == '>':
            tmp[j] = '^'
    program.append(tmp)

for i in range(m-1, -1, -1):
    for j in range(n):
        print(program[j][i], end= '')
    print()