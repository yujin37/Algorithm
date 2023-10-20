n, m = map(int,input().split())
DNA = []
for i in range(n):
    DNA.append(input())
distance = ''
dna = ['A', 'C', 'G', 'T']
result = 0
for i in range(m):
    a,t,g,c = 0,0,0,0
    for j in range(n):
        if DNA[j][i] == 'A':
            a+= 1
        elif DNA[j][i] == 'T':
            t+=1
        elif DNA[j][i] == 'G':
            g+=1
        elif DNA[j][i] == 'C':
            c+=1
    count = [a,c,g,t]
    tmp = dna[count.index(max(count))]
    distance += tmp
    
    for k in range(n):
        if DNA[k][i] != tmp:
            result += 1
print(distance)
print(result)