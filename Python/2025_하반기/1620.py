import sys
input = sys.stdin.readline
n, m = map(int,input().split())
poketmon_name = dict()
poketmon_index = dict()
for i in range(1,n+1):
    name = input().strip()
    poketmon_index[name] = i
    poketmon_name[i] = name

for j in range(m):
    question = input().strip()
    if question.isdigit():
        result = poketmon_name.get(int(question))
        print(result)
    elif question.isalpha():
        result = poketmon_index.get(question)
        print(result)