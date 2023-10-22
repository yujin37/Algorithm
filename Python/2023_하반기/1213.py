name = list(input())

check = {}
for i in range(len(name)):
    if name[i] in check:
        check[name[i]]+=1
    else:
        check[name[i]] = 1
cnt = 0 #홀수 갯수
mid = ''
for key, value in check.items():
    if value % 2 == 1: #0으로 안나누어 떨어지면
        mid += key
        cnt += 1 #더한다
if cnt>=2:
    print('I\'m Sorry Hansoo')
else:
    #print(sorted(check.items() , key=lambda x: (-x[1], x[0])))
    result = ''
    for key, value in sorted(check.items()):
        result += key * (value//2)
    print(result + mid + result[::-1])
 