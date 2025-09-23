import sys
input = sys.stdin.readline


n = int(input())
company_log = set()
for i in range(n):
    name, status = input().split()
    if status == 'enter':
        company_log.add(name)
    elif status == 'leave':
        
        company_log.remove(name)
sorted_name = sorted(list(company_log), reverse=True)
for result in sorted_name:
    print(result)