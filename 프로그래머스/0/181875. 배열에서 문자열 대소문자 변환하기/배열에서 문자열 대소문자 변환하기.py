def solution(strArr):
    
    ans = []
    
    for i, s in enumerate(strArr):
        if i % 2 ==0:
            ans.append(s.lower())
        else:
            ans.append(s.upper())
        
    
    
    return ans