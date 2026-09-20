def solution(l, r):
    answer = []

    for n in range(l,r+1):
        key1 = {"0","5"}
        key2 = {"5"}
        if set(str(n)) == key1 or set(str(n)) ==key2:
            answer.append(n)
    
    return answer if answer else [-1]