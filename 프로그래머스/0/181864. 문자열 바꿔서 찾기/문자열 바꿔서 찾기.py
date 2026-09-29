def solution(myString, pat):
    
    re_pat = "".join(["A" if c=="B" else "B" for c in pat])
    
    return int(re_pat in myString)