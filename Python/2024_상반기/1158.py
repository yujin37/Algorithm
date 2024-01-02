n, k = map(int,input().split())

circle = [i for i in range(1,n+1)]

now = 0
result = ''
result += '<'

while circle:
    now = (now + k-1) % len(circle)
    result += str(circle.pop(now)) + ', '
result = result[:-2] + '>'

print(result)
