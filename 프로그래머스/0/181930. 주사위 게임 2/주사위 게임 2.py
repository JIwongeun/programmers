def solution(a, b, c):
    
    check = len(set([a,b,c]))
    if check ==1:
        return (a+b+c)*(a**2 + b**2 + c**2)*(a**3 + b**3 + c**3)
    if check ==2:
        return (a+b+c)*(a**2 + b**2 + c**2)
    
    return (a+b+c)