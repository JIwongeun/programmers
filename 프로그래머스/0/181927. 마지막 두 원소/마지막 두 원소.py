def solution(num_list):
    answer = num_list
    
    ln, pn = num_list[-1], num_list[-2]
    
    if ln > pn:
        answer.append(ln-pn)
    else:
        answer.append(ln*2)
    
    return answer