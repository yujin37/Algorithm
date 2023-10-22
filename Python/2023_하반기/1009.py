n = int(input())
for i in range(n):
    a, b = map(int,input().split())
    a = a%10
    if a == 0:
        result = 10
    elif a== 1 or a == 5 or a == 6:
        result = a
    elif a== 4 or a == 9:
        b = b%2
        if b == 1:
            result = a
        else:
            result = (a*a) % 10

    else:
        b = b%4
        if b == 0:
            result = (a**4) % 10 % 10 % 10
        else:
            result = (a**b) % 10 % 10 % 10
    print(result)