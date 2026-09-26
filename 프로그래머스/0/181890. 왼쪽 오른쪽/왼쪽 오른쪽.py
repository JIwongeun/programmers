def solution(sl):

    if "l" in sl:
        if "r" in sl:
            return sl[:sl.index("l")] if sl.index("l") < sl.index("r") else sl[sl.index("r")+1:]
        else:
            return sl[:sl.index("l")]
    
    if "r" in sl:
        return sl[sl.index("r")+1:]
        
    
    return []