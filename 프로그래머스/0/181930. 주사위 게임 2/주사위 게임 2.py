def solution(a, b, c):
    
    if a==b and b==c: return (a + b + c) * (a*a + b*b + c*c) * (a*a*a + b*b*b + c*c*c)

    elif (a==b and b!=c) or (b==c and c!=a) or (c==a and a!=b):
        return (a + b + c) * (a*a + b*b + c*c)
   
    
    return (a + b + c)