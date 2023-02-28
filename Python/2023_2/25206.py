total, cnt = 0, 0
for i in range(20):
    name, grade, result = input().split()
    if result == 'A+':
        now=4.5
    elif result == 'A0':
        now=4.0
    elif result == 'B+':
        now=3.5
    elif result == 'B0':
        now=3.0
    elif result == 'C+':
        now=2.5
    elif result == 'C0':
        now=2.0
    elif result == 'D+':
        now=1.5
    elif result == 'D0':
        now=1.0
    elif result == 'F':
        now=0
    else:
        pass
    if result != 'P':
        total=total+(float(grade)*now)
        cnt=cnt+float(grade)
total_cnt=total/cnt
print(round(total_cnt, 6))