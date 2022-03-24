#단어정렬
n=int(input())
dic=[]

for i in range(n):
    dic.append(input())
dic_1=sorted(list(set(dic)))#중복제거, 리스트화, 그리고알파벳순으로 정렬하고
dic_1.sort(key=len)#길이순으로 정렬
for i in dic_1:#안에 있는 것을 출력해줌
    print(i)
