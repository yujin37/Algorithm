s = input()
n_list = [int(s[0]), int(s[:2]), int(s[:3])] #경우의 수 만들고
print(n_list)
flag = 0
for n in n_list:
    m = n
    new_num = ''
    while len(new_num) < len(s): #모양이 하나씩 쌓아 올라가면서 같은 게 있는지 체크
        new_num += str(m)
        if new_num == s:
            print(n, m)
            flag = 1
            break
        m += 1
    if flag == 1:
        break

    