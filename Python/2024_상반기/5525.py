import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
s = input().rstrip()
pk_len = 0
cnt = 0
for i in range(m):
    if pk_len % 2 == 0 and s[i] == 'I': #길이가 짝수이면 I가 나와야 하고
        pk_len += 1
    elif pk_len % 2 == 1 and s[i] == 'O': #길이가 홀수이면 O가 나와야 한다.
        pk_len += 1
    else: #만약에 그 글이가 끝나게 되면
        k = (pk_len - 1) // 2  #일단 절반으로 나누고
        if k >= n: #기준 길이보다 긴지 확인해서
            cnt += (k-n+1) #값 계산해주고
        pk_len = 0 #초기화
        if pk_len % 2 == 0 and s[i] == 'I': #그리고 다시 시작점인지 체크해서
            pk_len += 1 #길이를 추가
k = max(0,(pk_len - 1) // 2 ) #만약 끝까지 만족하면 한번 더 계산해준다.
if k >= n:
    cnt += (k-n+1)
print(cnt)
