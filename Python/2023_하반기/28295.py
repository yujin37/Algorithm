now = 0
for i in range(10):
    where = ['N', 'E', 'S', 'W']
    info = int(input())
    if info == 1: #우향우
        now += 1
        #print('우향우', now)
    elif info == 2: #뒤로 돌아
        now += 2
        #print('뒤로돌아', now)
    elif info == 3: #좌향좌
        now-=1
        #print('좌향좌', now)
    else:
        pass
    if now >= 4:
        now -= 4
    elif now < 0:
        now = 3
print(where[now])
    
    
    
    