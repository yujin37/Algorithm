a, d, k = map(int,input().split())

#일단 확률로 변환하고
d /= 100
k /= 100
result = 0 #이건 ㅣ결과값
i = 1
now = 1
while True:

    result += i * a * d *now #시간*몇번째*현재 확률* 이전판 질 확률 

    i+= 1
    if d == 1: #확률이 1이 넘어가면 중단한다.
        break
    now *= (1-d) #이전 판질 확률
    d += d*k # 이번 판 이길 확률
    if d>= 1: #확률이 초과되면 맞춰주고
        d = 1
print('%.7f' %result) #7자리 맞춰준다.