s = input()

word = ""


result = ""

flag = 0
for str in s:
    if str == ' ' and flag == 0: 
        word = word[::-1]
        result += (word +str)
        word = ""
    elif str == "<":
        word = word[::-1]
        result += (word + str)
        word = ""
        flag = 1
        
    elif str == ">":
        result += word + str
        word = ""
        flag = 0
    
    else:
        word += str
result += word[::-1]
print(result)