def solution(num_list):
    
    n1 = pow(sum(num_list),2)
    n2 = 1
    for n in num_list:
        n2 *= n
    
    
    return 1 if n1>n2 else 0