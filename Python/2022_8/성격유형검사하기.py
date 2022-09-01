def solution(survey, choices):
    test={'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    #test1={'R':0, 'T':0}
    #test2={'C':0, 'F':0}
    #test3={'J':0, 'M':0}
    #test4={'A':0, 'N':0}
    answer = ''
    for i in range(len(survey)):
        if choices[i]==1:
            test[survey[i][0]]+=3
        elif choices[i]==2:
            test[survey[i][0]]+=2
        elif choices[i]==3:
            test[survey[i][0]]+=1
        elif choices[i]==5:
            test[survey[i][1]]+=1
        elif choices[i]==6:
            test[survey[i][1]]+=2
        elif choices[i]==7:
            test[survey[i][1]]+=3

    answer+= "R" if test['R']>=test['T'] else "T"
    answer+= "C" if test['C']>=test['F'] else "F"
    answer+= "J" if test['J']>=test['M'] else "M"
    answer+= "A" if test['A']>=test['N'] else "N"
        
    return answer
