def solution(n_str):
    answer = ''
    
    for i, s in enumerate(n_str):
        if s == '0':
            continue
        else:
            return n_str[i:]
    