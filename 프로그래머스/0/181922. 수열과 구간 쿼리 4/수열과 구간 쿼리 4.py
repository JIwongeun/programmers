def solution(arr, queries):
    
    for s, e, k in queries:
        for i, n in enumerate(arr[s:e+1]):
            if (i+s)%k == 0 :
                arr[i] +=1
                
    return arr