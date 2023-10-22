import datetime
n = int(input())
program = []
for i in range(0, n):
    tmp = input().split()
    
    year, month, day = map(int,tmp[0].split('/'))
    hour, minute, second = map(int,tmp[1].split(':'))
    level = int(tmp[2])
    program.append((datetime.datetime(year, month, day, hour, minute, second), level))

program.sort()

default = datetime.timedelta(days=365)

temp_up, temp_down = 0, 0
idx = n-1
if program:
    for i in range(n):
        now, target = program[i], program[-1]
        temp = (target[0] - now[0])/ default
        force = max(0.5**float(temp), 0.9**(idx))
        temp_up += force * program[i][1]
        temp_down += force
        idx -=1
    print(round(temp_up/temp_down))
else:
    print(0)