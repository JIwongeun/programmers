def solution(my_string, queries):
    
    ml = list(my_string)
    
    for q in queries:
        s, e = q[0], q[1]
      
        ml[s:e+1] = ml[s:e+1][::-1]
    
    return ''.join(ml)