def solution(l, r):
    answer = []

    for n in range(l,r+1):
        key = {"0","5"}
        
        if not (set(str(n)) - key):
            answer.append(n)
    
    return answer if answer else [-1]