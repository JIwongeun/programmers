def solution(sl):

    for i, s in enumerate(sl):
        if s == "l":
            return sl[:i]
        if s == "r":
            return sl[i+1:]
        
        if "l" not in sl and "r" not in sl:
            break
        
    return []