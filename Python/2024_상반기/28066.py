def sum_num(n):
    num = 0
    for i in n:
        if i.isdigit():
            num+=int(i)
    return num
n = int(input())
result = list()
for i in range(n):
    cirel = input()
    result.append(cirel)
    
result.sort(key = lambda x:(len(x), sum_num(x), x))

for number in result:
    print(number)