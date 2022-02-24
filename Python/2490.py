#윷놀이, 파이썬은 0을 카운트하는 방식으로 진행해도 가능 .count(어떤 것) 방식
for i in range(3):
    a=list(map(int,input().split()))

    if a.count(0)==1: print("A")
    elif a.count(0)==2: print("B")
    elif a.count(0)==3: print("C")
    elif a.count(0)==4: print("D")
    else: print("E")
