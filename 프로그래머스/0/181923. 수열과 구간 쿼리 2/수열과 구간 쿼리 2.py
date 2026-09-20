def solution(arr, queries):
    
    answer = []
    for s, e, k in queries:
        tmp = []
        for n in arr[s:e+1]:
            if n>k:
                tmp.append(n)
        
        if len(tmp) > 0:
            answer.append(min(tmp))
        else:
            answer.append(-1)
        
    return answer