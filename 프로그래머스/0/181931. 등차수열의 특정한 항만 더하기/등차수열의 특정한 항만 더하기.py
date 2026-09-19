def solution(a, d, included):
    nl = [a+d*i for i in range(len(included))]
    
    answer = sum([x*y for x, y in zip(nl, included)])
    
    return answer