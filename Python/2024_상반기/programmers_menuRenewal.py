from itertools import combinations
def solution(orders, course):
    answer = []
    sets = dict()
    for order in orders:
        menu_list = []
        for i in range(len(course)):
            cases = list(combinations(order, course[i]))
            #print(cases)
            menu_list.extend(cases)
          
        for menu in menu_list:
            set_menu = ''.join(sorted(menu))

            if set_menu in sets:
                sets[set_menu] += 1
            else:
                sets[set_menu] = 1
    setMenu = dict()
    for number in course:
        temp = []
        temp_num = 0 
        for idx, value in sets.items():
            if number == len(idx) and value > temp_num and value > 1:
                temp = [idx]
                temp_num = value
            elif number == len(idx) and value == temp_num and value > 1:
                temp.append(idx)
        answer.extend(temp)
        #if value > 1:
        #    setMenu[idx] = value
    answer.sort()

    return answer