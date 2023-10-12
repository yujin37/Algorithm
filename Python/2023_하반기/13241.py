def gcd(a,b):
    while b >0:
        a,b = b, a%b
    return a
a, b = map(int,input().split())
if b%a == 0:
    result = b
else:
    result = a*b / gcd(a,b)
print(int(result))