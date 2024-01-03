n, m = map(int,input().split())

member = list(map(int,input().split()))
member.sort()

left, right = 0, len(member) - 1
cnt = 0


while left < right:
    
    team = member[left] + member[right] 
    
    if team < m:
        left += 1
    else: #능력치가 m 이상이면
        cnt += 1
        left += 1
        right -= 1
        
print(cnt)
