def solution(arr, k):
    answer = []
    
    num = list(dict.fromkeys(arr))
    
    for i in range(k):
        if i>=len(num):
            answer+=[-1]
        else:
            answer+=[num[i]]
    
    return answer