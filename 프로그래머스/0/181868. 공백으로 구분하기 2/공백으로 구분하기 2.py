def solution(my_string):
    
    answer = []
    ch = ""
    
    for i, s in enumerate(my_string):
        if s==" ":
            if ch != "":
                answer.append(ch)
                ch = ""
            continue
        else:
            ch += s
            
    if ch != "":
         answer.append(ch)   
    
    
    return answer