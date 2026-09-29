def solution(myString, pat):
    
    idx = "".join(reversed(myString)).index("".join(reversed(pat)))
        
    return myString[:len(myString)-idx]