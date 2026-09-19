def solution(code):
    ret = ""
    mode = 0
    for i in range(len(code)):
        if code[i] == "1":
            if mode:
                mode = 0
            else:
                mode = 1
                
        if code[i]!="1":
            if mode == 0 and i%2 ==0:
                ret = ret+code[i]

            if mode ==1 and i%2 ==1:
                ret = ret+code[i]
        
    
    return ret if ret != "" else "EMPTY"