def solution(myStr):
    answer = []
    st = ""
    for n in myStr:
        if n!='a' and n!='b' and n!='c':
            st += n
        else:
            if st:
                answer.append(st)
            st = ""
            
    if st:
        answer.append(st)
    
    return answer if answer else ["EMPTY"]