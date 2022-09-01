def solution(new_id):
    answer = ''
    test=['-','_','.']
    #1
    new_ids=new_id.lower()
    #2
    for i in new_ids:
        if i.isdigit() or i.isalpha() or i in test:
            answer+=i
    #3
    while '..' in answer:
        answer=answer.replace('..','.')
    #4
    if answer[0]=='.':
        answer=answer[1:] if len(answer)>1 else '.'
    if answer[-1]=='.':
        answer=answer[:-1]
    if answer=='':
        answer='a'
    if len(answer)>=16:
        answer=answer[:15]
        if answer[-1]=='.':
            answer=answer[:-1]
    
    while len(answer)<3:
        answer+=answer[-1]
    return answer
