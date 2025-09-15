n = int(input())
fibo = [0 for _ in range(n+1)]
fibo[0], fibo[1] = 0, 1

for i in range(2,n+1):
    F_n = fibo[i-1] + fibo[i-2]
    fibo[i] = F_n 
print(fibo[-1])