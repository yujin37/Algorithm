n = int(input())
m = int(input())

clothes = list(map(int,input().split()))
clothes.sort()

left, right = 0, len(clothes)-1

cnt = 0 # 갑옷의 개수



while left < right:
    sum = clothes[left] + clothes[right]
    
    if sum < m:
        left += 1
    elif sum > m:
        right -= 1
    else:
        cnt += 1
        left += 1
        right -= 1
    
print(cnt)
