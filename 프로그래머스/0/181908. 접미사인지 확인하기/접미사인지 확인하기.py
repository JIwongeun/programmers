def solution(my_string, is_suffix):
    answer = 0
    
    ss = [my_string[i:] for i in range(len(my_string))]

    
   
    return 1 if is_suffix in ss else 0