import sys
input = sys.stdin.readline

n, m = map(int,input().split())

member = dict()

#듣도 못한 사람
for i in range(n):
    name = input().replace("\n", "")
    member[name] = 1

#보도 못한 사람
for j in range(m):
    name = input().replace("\n", "")
    
    if member.get(name):
        member[name] += 1
    else:
        member[name] = 1
result = []
for (key, value) in member.items():
    if value == 2:
        result.append(key)
print(len(result))
result.sort()
for member_list in result:
    print(member_list)