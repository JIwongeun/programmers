def solution(num_list):
    
    n1 = 0
    n2 = 0
    
    for n in num_list:
        if n % 2 == 0:
            n2 = n2*10 + n
        else:
            n1 = n1*10 + n
    
    return n1+n2