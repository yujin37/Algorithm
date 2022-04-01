#다시풀기
#일곱난쟁이
list=[int(input()) for i in range(9)]
total=sum(list)

for i in range(9):
    for j in range(i+1,9):
        if (100==total-(list[i]+list[j])):
            n1,n2=list[i],list[j]
            list.remove(n1)
            list.remove(n2)
            list.sort()
            for i in range(len(list)):
                print(list[i])
            break
    if(len(list)<9):
        break

  

