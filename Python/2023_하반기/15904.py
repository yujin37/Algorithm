sen = input()
result = ''
now = 0
for char in sen:
    if now == 0 and char == 'U':
        result += 'U'
        now += 1
    elif (now == 1 or now == 3)and char == "C":
        result += 'C'
        now+=1
        if now == 3:
            break
    elif now == 2 and char == "P":
        result += 'P'
        now+=1
    else:
        pass
if result == 'UCPC':
    print('I love UCPC')
else:
    print('I hate UCPC')